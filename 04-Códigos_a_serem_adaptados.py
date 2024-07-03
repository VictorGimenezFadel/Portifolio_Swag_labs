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



