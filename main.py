import time

from Utils import Utils
from chrome import SeleniumChrome

print(' .  .  . iniciando bot selenium . . .')

utils = Utils()
botChrome = SeleniumChrome(utils.DRIVE_CHROME, utils.LINK_ACESSO)

if botChrome.login('alencar.machado@ufsm.br', 'alemac147'):
    botChrome.click_menu_lateral('Administração')
    botChrome.click_menu_lateral('Empresa')
    botChrome.click_menu_lateral('Cadastrar Empresa')
    botChrome.cadastrar_empresa()
else:
    print('erro no login')
    botChrome.aplication.quit()

time.sleep(5)
botChrome.aplication.quit()