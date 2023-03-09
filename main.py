import authentication
import landing
import menu


landing.init()
# authentication.main()


print('Select Action:')
for item in menu.data:
    print('[' + str(item['index']) + '] ' + item['name'])

selectedAction = False
while selectedAction == False:
    inputTargetFile = input("Select File [ID] : ")
    valueInputTargetFile = int(inputTargetFile) - 1
    if (valueInputTargetFile < len(menu.data)):
        selectedAction = inputTargetFile
        print('Selected Action : ' + menu.data[valueInputTargetFile]['name'])
    else:
        print('Invalid Index, try again...')
