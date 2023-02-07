from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
from notify_run import Notify
import streamlit as s
from streamlit_option_menu import option_menu
s.title("FIFA WEBSCRAPING")



start_button = s.button("Start BOT")
button_clicked = True
if start_button :
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    driver.get("https://l.facebook.com/l.php?u=https%3A%2F%2Fqueueing.fcwc2022.com%2F0725%2FinQueue%2F568%2Ffr%2F%3Forigin%3Dhttps%253A%252F%252Fticket.fcwc2022.com%253A3451%252Fshop%252FfListeManifs.aspx%253Fidstructure%253D0725%26fbclid%3DIwAR1lq6x_tQ3PgRoPZbOI3gLd_eueugbQOv75toup3AalVpVHwpxLCMAp1hI&h=AT1hvqOt2hvwE0BDoF3Etx84qOwVpxAqVmzTgJ2mYnJuoW-yR6i_c9UHLjjXjvpQCYc2jOwc4YQKlRcu2Nol8Ad4bxKV1eY7QBLHEGKzGQ04zJQbI_AZ3r-90cJ4Z0PivAKHhw")
    # driver.get("https://l.facebook.com/l.php?u=https%3A%2F%2Fticket.fcwc2022.com%2Fshop%2FfListeManifs.aspx%3Fidstructure%3D0725%26EventId%3D0%26request%3DQcE%2520w0WHSuBwZh1fkMAPgy%2520zUyJ1qt6z%26tn%3D912404%26quHash%3D2fecd8b1783ecd9566fc8ececb2879689713ab21bfc7094c9bda38d3b7e951fc%26fbclid%3DIwAR1BpCR0N67HC7RR9uJPG1Ob4FtsgR4pqiDKlT9ZIpxT8iD2uMt_82GhGdY&h=AT1eZWHr5wX24iURtwxVTxBygm2IFRbHsFIAlgDv63z5e5wJvqoFR43gYY1Xe4phkY_DKeP9FTvCCouHxGe4CDEAFbHhWqCXrLQE3hEAHE-NST1xxI2cC8qhT-RlIsVoLqe4Rw")
    status = False
    while button_clicked:
        time.sleep(10)
        content = driver.page_source
        soup = BeautifulSoup(content, features="lxml")
        try:
            final_match = soup.find(eventid="6")
            s.write(final_match.text, '\n')
            if "Indisponible" not in final_match.text:
                status = True
                s.write("TICKEYAT RAHOM HNA", '\n')
                notify = Notify()
                notify.send("TICKEYAT RAHOM HNA")

                time.sleep(5)

            # oth = soup.find('div', attrs={'class': 'col-sm-3 vcenter eventBtns'})
            # print(oth.text, '\n')
        

        except:
            s.write('ERROR OCCURED')

    # if status:
    #     time.sleep(1200)

        if not status:
            # Get the current browser window
            browser = driver.current_window_handle
            # Refresh the page
            driver.refresh()



