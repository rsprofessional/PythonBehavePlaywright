import pylab as p
from playwright.sync_api import sync_playwright



class ApiTesting:

    def testing_api_get(self):
        with sync_playwright() as p:
            # self.playwright = sync_playwright().start()
            context_request = p.request.new_context()
            response = context_request.get("http://localhost:8080/api/users/1")

            print(f'>>>> {response.status}')
            assert response.status == 200
            print(f"{response.text()}")
            text = response.text()
            print(text)
            response_id = response.json().get("id")
            print(f"id: {response_id}")
            print("")

    def testing_api_get_one_user_del(self,user):
        with sync_playwright() as one:
            context_request = one.request.new_context()
            response = context_request.get("http://localhost:8080/api/users")
            print(f'>>>> {response.status}')
            assert response.status == 200

            print(f"{response.json()}")
            email_procurado = user
            users = response.json()
            for user in users:
                if user["email"] == email_procurado:
                    user_id = user["id"]
                    print(user_id)
                    response_delete = context_request.delete(f"http://localhost:8080/api/users/{user_id}")
                    assert response_delete.status == 200
                    break

    # def testing_api_del(self):
    #     with sync_playwright() as one:
    #         user_del = self.testing_api_get_one_user()
    #         context_request = one.request.new_context()
    #         response = context_request.delete(f"http://localhost:8080/api/users/{user_del}")
    #
    #         assert response.status == 201
    #         print(f'user create: {response.status}')

    def testing_api_close(self):
        p.close()

    def testing_api_post(self):
        with sync_playwright() as delete_one:
         context_request = delete_one.request.new_context()
         response = context_request.post("http://localhost:8080/api/users", data={
            "email": "raulsantos@gmail.com",
            "firstName": "Raul",
            "lastName": "Santos"
         }, headers={'Content-Type':'application/json'})

         assert response.status == 201
         print(f'user create: {response.status}')
         print(response)
         print('')




