import os
from typing import Optional
from infrastructure.dtos.run import Run
from infrastructure.dtos.chat_message import ChatMessage
from infrastructure.dtos.chat_message_origin_and_generate import ChatMessageOriginAndGenerate
from openai import OpenAI
from data.services.sql_connection_service import SqlConnectionService
import uuid


class RunService():

    connection: SqlConnectionService
    assistant: OpenAI

    def __init__(self) -> None:
        self.assistant = OpenAI(api_key=os.environ.getenv('OPEN_AI_KEY'))

        self.connection = SqlConnectionService()

    async def run(
            self, 
            run_uuid: str, 
            chat_uuid: str, 
            route_scraps: list[object], 
            site_data=list[object],
            current_route_url= Optional[str],
            css_style_sheets= Optional[object]
        ):

        run: Run = Run(
            uuid=run_uuid,
            running_status= 'running',
            chat_uuid=chat_uuid
        )

        route_scraps_contents: list[str] = []

        css_style_sheet_contents: list[str] = []

        for item in css_style_sheets:
            css_style_sheet_content = '- '

            css_style_sheet_content = f' o nome do css é {item["style_sheet_name"]}, ' if item['style_sheet_name'] else '' 

            css_style_sheet_content = f' a url do css é {item["style_sheet_url"]}, ' if item['style_sheet_url'] else '' 

            css_style_sheet_content = f' a descrição do css é {item["style_sheet_description"]}, ' if item['style_sheet_description'] else '' 

            css_style_sheet_content = f'- '

            css_style_sheet_contents.append(css_style_sheet_content)

        for item in route_scraps:
            route_scrap_content = '- '

            route_scrap_content += f'a uuid (identificação no banco de dados) do componente é "{item["item_uuid"]}", ' if item['item_uuid'] else ''

            route_scrap_content += f'a identificação(id) do componente é "{item["item_id"]}", ' if item['item_id'] else ''

            route_scrap_content += f'a tag do componente é "{item["tag"]}", ' if item['tag'] else ''
            
            route_scrap_content += f'a classe css deste componente é "{item["css_class"]}", ' if item['css_class'] else ''

            route_scrap_content += f'a sua função deste componente na página é "{item["function_on_the_page"]}", ' if item['function_on_the_page'] else ''

            route_scrap_content += f'o componente pai deste componene possui o uuid (identificação do banco de dados) "{item["parent_uuid"]}", ' if item['parent_uuid'] else ''

            route_scrap_content += f'o seu título deste componente é "{item["title"]}", ' if item['title'] else ''

            route_scrap_content += f'o seu conteúdo deste componente é "{item["content"]}", ' if item['content'] else ''

            route_scrap_content += f'a sua descrição (o que é e/ou o que faz) deste componente é "{item["scrap_description"]}", ' if item['scrap_description'] else ''

            route_scrap_content += f'a url (endereço) da página a qual este componente pertence é "{item["route_url"]}"' if item['route_url'] else ''

            route_scrap_content += ';'

            route_scraps_contents.append(route_scrap_content)

        await self.connection.insert([run])

        statement = f"""
            SELECT chat_role, content, device_origin, uuid
            FROM chat_message 
            WHERE chat_uuid='{chat_uuid}' AND chat_role='user' ORDER BY id DESC LIMIT 1;"""

        last_message = await self.connection.get_one(statement)

        messages = [{'role': last_message[0], 'content': last_message[1]}]

        site_urls = '\n'.join([f'- Descrição da página: {item["route_description"]}, endereço da página: {item["route_url"]};' for item in site_data])

        configuration_message = f"""Como um especialista em auxílio na utilização de sites, você está aqui para fornecer suporte e orientação.
A seguir estão as URLs disponíveis para referência:\n{site_urls}\n
Posso esclarecer dúvidas e fornecer URLs relevantes quando necessário.
Quando um usuário expressar interesse em acessar uma página específica, utilize a função \"go_to_page\" para direcioná-lo para o destino desejado, baseando-se na descrição da página fornecida pelo usuário. 
Além disso, estou aqui para responder qualquer outra dúvida que você possa ter e oferecer orientações adicionais, se necessário. 
Se precisar, posso personalizar o CSS do site conforme suas solicitações. 
Você pode me enviar as especificações ou um link para uma folha de estilo CSS existente. 
Além disso, tenho a capacidade de criar códigos JavaScript personalizados com base nas suas necessidades. 
Se precisar, posso usar referências aos componentes da página para garantir que os códigos sejam precisos e eficientes. 
"""
        
        if last_message: 
           configuration_message += f"\nO usuário está se comunicando através de um dispositivo {last_message[2]}.\n"
        
        if current_route_url:
            configuration_message += f"\n A página atual é '{current_route_url}'.\n"

        if(len(css_style_sheet_contents) > 0):
            content = '\n'.join(css_style_sheet_contents)

            configuration_message += f"""
A seguir estão os links de folhas de estilo CSS disponíveis para este site:
\n{content}\n
Quando o usuário solictar alguma alteração no estilo, verifique nos estilos acima qual o mais coerente a ser aplicado.
O css pode ser adicionado ao site ou substituir todo o css que o site.
Você deve utilizar apenas os estilos fornecidos acima.
Utilize a função \"inject_css\" para enviar as alteraçõs do css.
\n"""

        if(len(route_scraps_contents) > 0):
            content ='\n'.join(route_scraps_contents)

            configuration_message += f"""
Tenho a capacidade de realizar a modificação dinâmica das páginas conforme as solicitações do usuário.
Os componentes disponíveis na página são os seguintes:\n{content}\n
Ao solicitar uma alteração, por favor, referencie apenas os componentes listados acima através da função \"edit_component\". Se um componente não estiver presente, instrua o usuário a cadastrá-lo.
É importante incluir o ID (se existir) e a classe CSS (se existir) ao fazer referência aos elementos, para facilitar sua localização na aplicação.
Quando um usuário solicitar uma mudança de cor, seja por código hexadecimal ou nome da cor em inglês, esteja preparado para realizar a alteração conforme solicitado.
Você tem autorização para ajustar a cor e visibilidade dos componentes listados de acordo com as preferências do usuário.
Além disso, você pode criar novos componentes HTML para serem inseridos, substituir componentes filhos dentro da página e remover todos os filhos de um componente, utilize a função \"inject_html\" para isso.
Estou à disposição para esclarecer quaisquer dúvidas sobre esses componentes."""
            
        messages.insert(0, {
            'role': 'system',
            'content': configuration_message
        })

        try:
            chat_response = self.assistant.chat.completions.create(
                model='gpt-4o',
                messages=messages,
                temperature=0,
                tools=self.tools
            )

            assistant_message = chat_response.choices[0].message

            generated_uuid = uuid.uuid4()

            assistant_message = chat_response.choices[0].message

            generated_uuid = uuid.uuid4()

            if assistant_message.content is not None:
                chat_message: ChatMessage = ChatMessage(
                    uuid=generated_uuid,
                    chat_uuid=chat_uuid,
                    chat_role='system',
                    tool_call=None,
                    content=assistant_message.content,
                    device_origin=None
                )

                await self.connection.insert([chat_message])

            if assistant_message.tool_calls is not None:
                tool_call = [{'arguments': a.function.arguments , 'name': a.function.name} for a in  assistant_message.tool_calls]

                chat_message: ChatMessage = ChatMessage(
                    uuid=generated_uuid,
                    chat_uuid=chat_uuid,
                    chat_role='system',
                    tool_call=f'{tool_call}',
                    device_origin=None,
                    content='Só um instante, já vou verificar para você.'
                ) 

                await self.connection.insert([chat_message])

            if last_message:
                try:
                    await self.connection.insert([ChatMessageOriginAndGenerate(
                        uuid=uuid.uuid4(),
                        origin_uuid=last_message[3],
                        generate_uuid=chat_message.uuid,
                    )])
                except Exception as e:
                        print(e)
                    
            statement = f"UPDATE run SET running_status='success' WHERE uuid='{run.uuid}'" 

            await self.connection.update(statement)

        except Exception as error:
            print("An error occurred:", error)

            statement = f"UPDATE run SET running_status='failed' WHERE uuid='{run.uuid}'"

            await self.connection.update(statement)

    tools = [
        {
        "type": "function",
        "function": {
            "name": "go_to_page",
            "description": "Retorna uma url com base nas perguntas feitas pelo usuário",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                            "type": "string",
                            "description": "A url para a página destino"
                        }
                    },
                "required": ["path"]
                }
            }
        },
        {
        "type": "function",
        "function": {
            "name": "inject_javascript",
            "description": "Retorna um código javascript de acordo com as solicitações do usuário",
            "parameters": {
                "type": "object",
                "properties": {
                    "script": {
                            "type": "string",
                            "description": "O código javascript a ser injetado"
                        }
                    },
                "required": ["script"]
                }
            }
        },
        {
        "type": "function",
        "function": {
            "name": "inject_css",
            "description": "Retorna uma url para um css, ou um css gerado, de acordo com as solicitações do usuário e os css disponíveis",
            "parameters": {
                "type": "object",
                "properties": {
                        "url": {
                            "type": "string",
                            "description": "A url para o css"
                        },
                        "component": {
                            "type": "string",
                            "description": "O id ou classe do componente que será afetado"
                        },
                        "generated": {
                            "type": "string",
                            "description": "Este é o css gerado que deverá ser aplicado na página"
                        },
                        "action": {
                            "type": "string",
                            "enum": ["merge", "replace"],
                            "description": "Este item define como o css será aplicado. \"merge\" define que o css deve ser mesclado ao existente,  \"replace\" define que o css existente deve ser substituido pelo novo"
                        }
                    },
                "required": ["action"]
                }
            }
        },
        {
        "type": "function",
        "function": {
            "name": "edit_component",
            "description": "Retorna os dados para a alteração de uma componente da página de acordo com a solicitação do usuário",
            "parameters": {
                "type": "object",
                "properties": {
                        "visibility": {
                            "type": "string",
                            "enum": ["visible", "hidden", "collapse"],
                            "description": "Esconde ou mostra um elemento sem alterar o documento"
                        },
                        "display": {
                            "type": "string",
                            "enum": ["none", "initial", "inline", "block", "contents"],
                            "description": "Define como o elemento será apresentado na página"
                        },
                        "color": {
                            "type": "string",
                            "description": "A cor do componente"
                        },
                        "css_class": {
                            "type": "string",
                            "description": "A classe css do componente"
                        },
                        "id": {
                            "type": "string",
                            "description": "A identificação(id) do componente"
                        }
                    }
                }
            } 
        },
        {
        "type": "function",
        "function": {
            "name": "inject_html",
            "description": "Retorna um código html a ser injetado na página e a identificação do componente (id e/ou class) que será alterado",
            "parameters": {
                "type": "object",
                "properties": {
                        "html_code": {
                            "type": "string",
                            "description": "O código html gerado"
                        },
                        "component_id": {
                            "type": "string",
                            "description": "O id do componente onde o html será inserido"
                        },
                        "component_class": {
                            "type": "string",
                            "description": "A classe do componente onde o html será inserido"
                        },
                        "position" :
                        {
                            "type": "string",
                            "enum": ["start", "end"],
                            "description": "Este item define a posição do item a ser adicinado ou remivido. Por padrão seu valor será \"end\""
                        },
                        "action" : {
                            "type": "string",
                            "enum": ["add", "replace_childrens", "clean", "delete"],
                            "description": "A ação a ser tomada, que pode ser \"add\" para adiconar um componente, \"replace_childrens\" para substituir os componentes filhos, \"clean\" para remover todos os componentes filhos ou \"delete\" para remover de um componente em um posição especificada pelo usuário (\"start\" para início \"end\" para ao fim, o valor padrãp é \"end\")"
                        }
                    },
                "required": ["html_code"]
                }
            }
        }
    ]