        #Entrar no carrinho
        entrar_carrinho = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
        entrar_carrinho.click()



        #Rolar toda para baixo
        browser.execute_script("window.scrollBy(0, 500);")
        WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "checkout"))) #Espera até que o elemento desejado seja visível na página



        #Realizar checkout
        btn_checkout = browser.find_element(By.ID, "checkout")
        btn_checkout.click()





        #Rolar toda tela para cima
        browser.execute_script("window.scrollBy(0, -500);")
        WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "first-name"))) #Espera até que o elemento desejado seja visível e clicavel na página



        #Checkout

        #Primeiro nome (Firt name)
        first_name = browser.find_element(By.ID, "first-name")
        first_name.send_keys("Victor Gimenez Fadel")



        #Apelido (Last name)
        last_name = browser.find_element(By.ID, "last-name")
        last_name.send_keys("Victor")



        #CEP (Zip/Postal Code)
        postal_code = browser.find_element(By.ID, "postal-code")
        postal_code.send_keys("12345678")



        #Rolar toda tela para baixo
        browser.execute_script("window.scrollBy(0, 500);")
        WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "continue"))) #Espera até que o elemento desejado seja visível e clicavel na página



        #Finalizar checkout (Continue)
        btn_continue = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "continue")))
        btn_continue.click()



        #Finalizar compra (Finish)
        btn_finish =WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "finish")))
        btn_finish.click()



        #Voltar para a página inicial (Back Home)
        btn_back_home = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID,"back-to-products")))
        btn_back_home.click()





        #Interação com o filtro

        #filtro
        filtro = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@class='product_sort_container']")))
        filtro.click()



        #Opção de Z a A
        optn_z_a = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//option[@value='za']")))
        optn_z_a.click()



        #Segunda interação com o Menu lateral (3 risquinhos)
        menu_lateral_esq = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
        menu_lateral_esq.click()



        #Opção About (Sobre)
        optn_about = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable(By.XPATH, "//a[@id='about_sidebar_link']"))
        optn_about.click()



