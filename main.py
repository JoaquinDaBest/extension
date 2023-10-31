import requests
import json
#rice is good!
print("Enter the id of the extension you want to install (ex. kbfnbcaeplbcioakkpcpgfkobkghlhen)")
extension_id = input(">")
print("\n")

r = requests.post(f"https://chrome.google.com/webstore/ajax/detail?hl=en&gl=US&pv=20210820&id={extension_id}&r=j") #google api
j = json.loads(r.text[6:]) #get json data from the google api
manifest = j[1][1][9][0].replace("\n","\\n").replace("'","\\'")
icon_url = j[1][1][0][3] #hopefully google doesn't change this
extension_name = j[1][1][0][1]

javascript_url = 'chrome.webstorePrivate.beginInstallWithManifest3({esbAllowlist:!0,iconUrl:"' + icon_url +'",id:"' + extension_id + '",localizedName:"' + extension_name + '",manifest:\'' + manifest +'\'},function(){chrome.webstorePrivate.completeInstall("' + extension_id + '", function() {console.log(arguments)})});'

print(javascript_url)

print("\n\n")
print("Visit https://chrome.google.com/webstore404page and type 'javascript:' in the URL bar followed by the text from above")
#joaquin
