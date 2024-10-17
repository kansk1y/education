import requests
import json

# Получаем токен авторизации (как в предыдущем примере)
url_login = "https://apigw.bi.group/clients/api/v3/mobile/User/loginExternal"

payload_login = json.dumps({
    "email": "",
    "password": ""
})
headers_login = {
    'Content-Type': 'application/json-patch+json',
    'accept': 'application/json'
}

response_login = requests.post(url_login, headers=headers_login, data=payload_login)

if response_login.status_code == 200:
    # Извлекаем токен из ответа
    token = response_login.json().get("token")
    print(f"Токен: {token}")

    # Список объектов, которые нужно обновить (например, 100 объектов)
    objects_to_update = [
        {"guaid_id": "d88232ad-20b5-11e1-b61c-1cc1debf0968", "data": True},
{"guaid_id": "462280da-e8b9-11e0-931e-1cc1debf0968", "data": True},
{"guaid_id": "7eae93fe-459f-11e1-8d0b-1cc1debf0968", "data": True},
{"guaid_id": "fadc9f8a-bea0-11e2-a87a-0025906b4dd5", "data": True},
{"guaid_id": "4842cfce-e49d-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "fadc9f8b-bea0-11e2-a87a-0025906b4dd5", "data": True},
{"guaid_id": "fadc9f8c-bea0-11e2-a87a-0025906b4dd5", "data": True},
{"guaid_id": "0d9efe24-c8cf-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "8cf852ee-c626-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "0d9efdec-c8cf-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "0d9efded-c8cf-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "f3c2781b-0f2d-11e4-882b-0025906b4dd5", "data": True},
{"guaid_id": "14dd4534-4867-11e4-a297-0025906b4dd5", "data": True},
{"guaid_id": "0d9efe25-c8cf-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "c9593220-6bb7-11e3-a09c-0025906b4dd5", "data": True},
{"guaid_id": "0d9efde6-c8cf-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "cbcad321-12f9-11e4-882b-0025906b4dd5", "data": True},
{"guaid_id": "0d9efe2b-c8cf-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "5ba2b3fb-c241-11e4-8539-0025906b4dd4", "data": True},
{"guaid_id": "fcf7f8a2-9a0c-11e4-bd2b-0025906b4dd5", "data": True},
{"guaid_id": "0d9efe13-c8cf-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "0d9efe1f-c8cf-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "0d9efde7-c8cf-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "3bd7b7d5-7b9c-11e5-b9a5-b4b52f5405e7", "data": True},
{"guaid_id": "0d9efe20-c8cf-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "5ba2b3fd-c241-11e4-8539-0025906b4dd4", "data": True},
{"guaid_id": "14dd4533-4867-11e4-a297-0025906b4dd5", "data": True},
{"guaid_id": "f1709d5e-97ea-11e4-bd2b-0025906b4dd5", "data": True},
{"guaid_id": "f707d413-1ca0-11e6-98fe-b4b52f5405e7", "data": True},
{"guaid_id": "463fe333-843b-11e5-b9a5-b4b52f5405e7", "data": True},
{"guaid_id": "69037606-876a-11e4-bd2b-0025906b4dd5", "data": True},
{"guaid_id": "f707d415-1ca0-11e6-98fe-b4b52f5405e7", "data": True},
{"guaid_id": "f707d414-1ca0-11e6-98fe-b4b52f5405e7", "data": True},
{"guaid_id": "6f4cd681-115c-11e4-882b-0025906b4dd5", "data": True},
{"guaid_id": "6f4cd680-115c-11e4-882b-0025906b4dd5", "data": True},
{"guaid_id": "0d9efe14-c8cf-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "6f4cd682-115c-11e4-882b-0025906b4dd5", "data": True},
{"guaid_id": "0d9efdeb-c8cf-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "00b06de6-d4d6-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "b14bdbd1-cc65-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "89bb290d-2d09-11e4-acc3-0025906b4dd5", "data": True},
{"guaid_id": "89bb290e-2d09-11e4-acc3-0025906b4dd5", "data": True},
{"guaid_id": "81c6b286-2593-11e6-98fe-b4b52f5405e7", "data": True},
{"guaid_id": "8d48cfdb-230e-11e6-98fe-b4b52f5405e7", "data": True},
{"guaid_id": "0d9efdfa-c8cf-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "284b3e36-3954-11e6-aa43-b4b52f5405e7", "data": True},
{"guaid_id": "97698862-230f-11e6-98fe-b4b52f5405e7", "data": True},
{"guaid_id": "0d9efe2c-c8cf-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "69037605-876a-11e4-bd2b-0025906b4dd5", "data": True},
{"guaid_id": "f1709d5b-97ea-11e4-bd2b-0025906b4dd5", "data": True},
{"guaid_id": "f1709d5c-97ea-11e4-bd2b-0025906b4dd5", "data": True},
{"guaid_id": "6f4cd66f-115c-11e4-882b-0025906b4dd5", "data": True},
{"guaid_id": "284b3e37-3954-11e6-aa43-b4b52f5405e7", "data": True},
{"guaid_id": "f1709d61-97ea-11e4-bd2b-0025906b4dd5", "data": True},
{"guaid_id": "43d4a8c5-8c7b-11e6-89ba-b4b52f5405e7", "data": True},
{"guaid_id": "27f51e20-4f48-11e7-826f-b4b52f5405e7", "data": True},
{"guaid_id": "0d9efde3-c8cf-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "ee11d40c-3703-11e8-80cf-bb580b2abfef", "data": True},
{"guaid_id": "3995281d-49d9-11e7-826f-b4b52f5405e7", "data": True},
{"guaid_id": "63e39cd7-89cb-11e4-bd2b-0025906b4dd5", "data": True},
{"guaid_id": "343c42b4-832a-11e7-826f-b4b52f5405e7", "data": True},
{"guaid_id": "0444d694-a373-11e7-80c9-001dd8b71c2c", "data": True},
{"guaid_id": "678d1c6d-2094-11e6-98fe-b4b52f5405e7", "data": True},
{"guaid_id": "0d9efe0a-c8cf-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "670d8aa4-1e6f-11e7-97ac-b4b52f5405e7", "data": True},
{"guaid_id": "d9b47e56-0b41-11e5-b0be-b4b52f5405e7", "data": True},
{"guaid_id": "0d9efe22-c8cf-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "0d9efe28-c8cf-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "ca20cae7-9cdb-11e6-97ac-b4b52f5405e7", "data": True},
{"guaid_id": "0d9efdcd-c8cf-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "27e5d8c1-2266-11e6-98fe-b4b52f5405e7", "data": True},
{"guaid_id": "e95a3082-7bbe-11e6-89ba-b4b52f5405e7", "data": True},
{"guaid_id": "e95a3083-7bbe-11e6-89ba-b4b52f5405e7", "data": True},
{"guaid_id": "7e5d8578-c3c6-11e4-b3af-0025906b4dd4", "data": True},
{"guaid_id": "7e5d857a-c3c6-11e4-b3af-0025906b4dd4", "data": True},
{"guaid_id": "0d9efde1-c8cf-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "c4c21dcc-ebda-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "e19adc1a-8607-11e6-89ba-b4b52f5405e7", "data": True},
{"guaid_id": "c0ae35c2-1af2-11e8-80cf-bb580b2abfef", "data": True},
{"guaid_id": "8c0b331c-4ed3-11e8-80cf-bb580b2abfef", "data": True},
{"guaid_id": "0d9efe29-c8cf-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "0d9efdff-c8cf-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "11a1c7ec-01d7-11e8-80cf-bb580b2abfef", "data": True},
{"guaid_id": "a2646e77-4a39-11e6-aa43-b4b52f5405e7", "data": True},
{"guaid_id": "1ef6c0e0-01bf-11e8-80cf-bb580b2abfef", "data": True},
{"guaid_id": "fe2c0317-e735-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "8219af68-e1a4-11e4-b0be-b4b52f5405e7", "data": True},
{"guaid_id": "8219af69-e1a4-11e4-b0be-b4b52f5405e7", "data": True},
{"guaid_id": "e30d3f42-4dd6-11e4-a297-0025906b4dd5", "data": True},
{"guaid_id": "8219af67-e1a4-11e4-b0be-b4b52f5405e7", "data": True},
{"guaid_id": "88eac272-4e13-11e4-a297-0025906b4dd5", "data": True},
{"guaid_id": "88eac273-4e13-11e4-a297-0025906b4dd5", "data": True},
{"guaid_id": "88eac274-4e13-11e4-a297-0025906b4dd5", "data": True},
{"guaid_id": "8219af6a-e1a4-11e4-b0be-b4b52f5405e7", "data": True},
{"guaid_id": "8219af6b-e1a4-11e4-b0be-b4b52f5405e7", "data": True},
{"guaid_id": "f322d99e-676c-11e2-9abb-0025906b4dd5", "data": True},
{"guaid_id": "efb8a0ea-66b8-11e2-a24a-0025906b4dd5", "data": True},
{"guaid_id": "bc98e672-a805-11e7-80c9-001dd8b71c2c", "data": True},
{"guaid_id": "fbf8625a-6523-11e2-9624-0025906b4dd5", "data": True},
{"guaid_id": "0d9efdaf-c8cf-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "07500c15-a2db-11e5-b9a5-b4b52f5405e7", "data": True},
{"guaid_id": "00fd6c20-1155-11e4-882b-0025906b4dd5", "data": True},
{"guaid_id": "0005afc7-2445-11e9-80d9-00155d101f25", "data": True},
{"guaid_id": "670d8aa5-1e6f-11e7-97ac-b4b52f5405e7", "data": True},
{"guaid_id": "0d9efdc0-c8cf-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "e3f6365e-8ecf-11ea-a830-00155d101559", "data": True},
{"guaid_id": "4f09f33e-7297-11e7-826f-b4b52f5405e7", "data": True},
{"guaid_id": "cc150e40-a4e0-11e6-97ac-b4b52f5405e7", "data": True},
{"guaid_id": "1adff438-19fb-11e7-97ac-b4b52f5405e7", "data": True},
{"guaid_id": "ddaa628d-0242-11e8-80cf-bb580b2abfef", "data": True},
{"guaid_id": "d937fff0-f19c-11ea-a830-00155d101559", "data": True},
{"guaid_id": "ddaa628e-0242-11e8-80cf-bb580b2abfef", "data": True},
{"guaid_id": "8621cc8c-f8dc-11ea-a837-00155d101d74", "data": True},
{"guaid_id": "a591a710-f903-11eb-a81e-001dd8b72708", "data": True},
{"guaid_id": "2425f309-f904-11eb-a81e-001dd8b72708", "data": True},
{"guaid_id": "f8f87e31-459f-11e9-80d9-00155d101f25", "data": True},
{"guaid_id": "3cd9c850-93d3-11e8-80d7-00155da7893d", "data": True},
{"guaid_id": "3228fe9d-5c36-11e9-80db-00155d10652f", "data": True},
{"guaid_id": "f8f87e32-459f-11e9-80d9-00155d101f25", "data": True},
{"guaid_id": "0d9efdcf-c8cf-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "ee517b4c-5b2c-11ed-a82b-001dd8b726aa", "data": True},
{"guaid_id": "3e0fdc14-f8cb-11e2-bee0-0025906b4dd5", "data": True},
{"guaid_id": "ed9b7095-062c-11e6-98fe-b4b52f5405e7", "data": True},
{"guaid_id": "89bb2910-2d09-11e4-acc3-0025906b4dd5", "data": True},
{"guaid_id": "89bb290f-2d09-11e4-acc3-0025906b4dd5", "data": True},
{"guaid_id": "0d9efdf0-c8cf-11e3-882b-0025906b4dd5", "data": True},
{"guaid_id": "219860a6-3824-11e4-a1b0-0025906b4dd5", "data": True},
{"guaid_id": "cbcad323-12f9-11e4-882b-0025906b4dd5", "data": True},
{"guaid_id": "a6dd6d8c-41a2-11e6-aa43-b4b52f5405e7", "data": True},
{"guaid_id": "009197d6-3bb8-11e7-826f-b4b52f5405e7", "data": True},
{"guaid_id": "35903a9d-bda7-11e4-8539-0025906b4dd4", "data": True},
{"guaid_id": "35903a9e-bda7-11e4-8539-0025906b4dd4", "data": True},
{"guaid_id": "4bffe18c-7cd9-11e7-826f-b4b52f5405e7", "data": True},
{"guaid_id": "5ba2b3fe-c241-11e4-8539-0025906b4dd4", "data": True},
{"guaid_id": "4632add4-6c1b-11e1-85c8-1cc1debf0968", "data": True}
        # Добавь сюда остальные 98 объектов
    ]

    # URL для обновления
    url_update_base = "https://apigw.bi.group/clients/api/v4/mobile/Telecom/{guaid_id}"

    headers_update = {
        'accept': '*/*',
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json-patch+json'
    }

    # Цикл для отправки запросов по каждому объекту
    for obj in objects_to_update:
        guaid_id = obj["guaid_id"]
        payload_update = json.dumps(obj["data"])

        # Формируем URL для каждого объекта
        url_update = url_update_base.replace("{guaid_id}", guaid_id)

        # Отправляем PUT-запрос для каждого объекта
        response_update = requests.put(url_update, headers=headers_update, data=payload_update)

        # Выводим результат для каждого запроса
        print(f"Обновление объекта {guaid_id}: {response_update.status_code}, {response_update.text}")

else:
    print(f"Ошибка авторизации: {response_login.status_code}, {response_login.text}")

