
from playwright.sync_api import sync_playwright, expect
import time



class ApiTesting:

    def create_user_validate_it(self):
    
        # Cria o usuário e pega o id
        user_id, email = self.testing_api_post()
        # Valida o usuário criado neste caso nao faz nada paenas recebe os parametros 
        self.testing_api_get(user_id, email)



    def testing_api_get(self, user_id, email):
        with sync_playwright() as p:
            # self.playwright = sync_playwright().start()
            
            context_request = p.request.new_context()
            response = context_request.get("https://gorest.co.in/public/v2/users",params={"email": email})
            print(response.json())
           
            assert response.status == 200
            print(f">>>> {response.status}")
            print(f'retorna o email do user {email}')
            print(f'retorna o id do user {user_id}')

            # users = response.json()
            # print(users)
            # if users:
            #     print(users[0])
            # else:
            #     print("Usuário não encontrado pelo filtro de email")

            # filtered_users = [
            #        user for user in users if user.get("email") == "raulsantos@gmail.com"
            #     ]

            # print(filtered_users)
            # id = filtered_users[0]["id"]
            # print(id)
            # assert first_name == "Raul"
           

            #  print("")

    # def close_api(self):
    #     self.context_request.dispose()
    #     self.playwright.stop()        

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

    #def testing_api_close(self):

         #p.close()

    def testing_api_post(self):
        with sync_playwright() as create_one:
         context_request = create_one.request.new_context()

        # 🔹 email dinâmico (sempre único)
         email = f"raul_{int(time.time())}@gmail.com"

         response = context_request.post("https://gorest.co.in/public/v2/users", data={
            "name": "Raul",
            "email": email,
            "gender": "male",
            "status": "active"
         }, 
         headers={ "Authorization": "Bearer 3203121efa247b3de86e9973aee21904ac4ef042e8b9527d9207f64b1a96ebd4",
                  'Content-Type':'application/json'})

         
         print(f'user create: {response.status}')
         assert response.status == 201
        #  print(response)
        #  print('')
         body = response.json()
         user_id = body["id"]
         email = body["email"]

         print(f"ID criado: {user_id}")
         print(f"Email criado: {email}")

         return user_id, email
        



   




