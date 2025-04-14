import json
import boto3
import uuid
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
tabela = dynamodb.Table('Produtos')

def lambda_handler(event, context):
    http_method = event['requestContext']['http']['method']
    path = event['rawPath']

    if http_method == 'GET' and path == '/prod/produtos':
        try:
            response = tabela.scan()
            produtos = response.get('Items', [])
            return {
                'statusCode': 200,
                'body': json.dumps(produtos, default=str)
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'mensagem': 'Erro interno', 'erro': str(e)})
            }

    elif http_method == 'POST' and path == '/prod/produtos':
        try:
            body = json.loads(event['body'], parse_float=Decimal)
            produto = {
                'id': str(uuid.uuid4()),
                'nome': body['nome'],
                'preco': body['preco']
            }
            tabela.put_item(Item=produto)
            return {
                'statusCode': 201,
                'body': json.dumps(produto, default=str)
            }
        except Exception as e:
            return {
                'statusCode': 500,
                'body': json.dumps({'mensagem': 'Erro interno', 'erro': str(e)})
            }

    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'mensagem': 'Rota não encontrada. Verifique o caminho e o método HTTP.'})
        }
