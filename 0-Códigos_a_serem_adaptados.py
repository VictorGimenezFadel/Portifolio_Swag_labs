 #Voltar para a tela anterior -Home (Back)
        browser.back()





        #Interação com o carrinho (ADD)

        #Adicionar item ao carrinho (Sauce Labs Backpack)
        add_carrinho_backpack = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
        add_carrinho_backpack.click()



        #Adicionar item ao carrinho (Sauce Labs Bike Light)
        add_carrinho_bike_light = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light")))
        add_carrinho_bike_light.click()



        #Adicionar item ao carrinho (Sauce Labs Onesie)
        browser.execute_script("window.scrollBy(0, 500);") #Rolar tela para baixo
        add_carrinho_onesie = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-onesie")))
        add_carrinho_onesie.click()



        #Rolar toda tela para cima
        browser.execute_script("window.scrollBy(0, -500);")
        WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))) #Espera até que o elemento desejado seja visível e clicavel na página





        #Dentro do carrinho - icone

        #Entrar no carrinho
        entrar_carrinho = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
        entrar_carrinho.click()



        #Remover item do carrinho (Bike)
        remover_item_bike = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "remove-sauce-labs-bike-light")))
        remover_item_bike.click()



        #Remover item do carrinho (Onesie)
        remover_item_onesie = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "remove-sauce-labs-onesie")))
        remover_item_onesie.click()



        #Voltar para a tela anterior - Home(Back)
        browser.back()



        #Adicionar item ao carrinho (Sauce Labs Fleece Jacket)
        add_carrinho_fleece_jacket = WebDriverWait(browser, 30).until(
            EC.visibility_of_element_located((By.ID, "add-to-cart-sauce-labs-fleece-jacket"))) #Espera até que o elemento desejado seja visível na página
        browser.execute_script("window.scrollBy(0, 200);")
        add_carrinho_fleece_jacket.click()



        #Adicionar item ao carrinho (Sauce Labs Bolt T-Shirt)
        add_carrinho_bolt_tshirt = WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")))
        add_carrinho_bolt_tshirt.click()



        #Rolar toda para cima
        browser.execute_script("window.scrollBy(0, -500);")
        WebDriverWait(browser, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))) #Espera até que o elemento desejado seja visível na página



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



