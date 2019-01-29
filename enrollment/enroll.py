import requests



headers = {
  "Accept": "*/*",
  "Accept-Encoding": "gzip, deflate, br",
  "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
  "Connection": "keep-alive",
  "Content-Length": "1715",
  "Content-Type": "application/x-www-form-urlencoded",
  "Host": "campus.rit.edu",
  "Origin": "https://campus.rit.edu",
  "Referer": "https://campus.rit.edu/psc/PRITXJ/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL?Page=SSR_SSENRL_CART&Action=A&ACAD_CAREER=GRAD&EMPLID=580000313&ENRL_REQUEST_ID=&INSTITUTION=RIT01&STRM=2175",
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"
}


cookies = {
  "BIGipServer~Private~mycampusadmin_rit_edu_20010": "rd2o00000000000000000000ffff819bb853o20018",
  "ExpirePage": "https://campus.rit.edu/psp/PRITXJ/",
  "LPVID": "A2NzY4NTEyZTdiYjJmODQ3",
  "PS_DEVICEFEATURES": "width:1366 height:768 pixelratio:1 touch:0 geolocation:1 websockets:1 webworkers:1 datepicker:1 dtpicker:1 timepicker:1 dnd:1 sessionstorage:1 localstorage:1 history:1 canvas:1 svg:1 postmessage:1 hc:0 maf:0",
  "PS_LOGINLIST": "https://campus.rit.edu/PRITXJ",
  "PS_TOKEN": "pgAAAAQDAgEBAAAAvAIAAAAAAAAsAAAABABTaGRyAk4AbQg4AC4AMQAwABQVvIvnUgPONX2CSVfgXvbThyx7KmYAAAAFAFNkYXRhWnicJYxNDkAwGERfS6zETTRUtRzAz0oEewuJnRs6nC81ybxZTGYeIE20UpKvJiq/uPEEalqygYWJYmVn5OBkZsNZKqkDpbAWVnSRHkMjM4ONdPTi/4oPazELTw==",
  "PS_TOKENEXPIRE": "08_Nov_2017_16:36:02_GMT",
  "SignOnDefault": "cf6715",
  "__qca": "P0-489312702-1503520668649",
  "__utma": "242358273.2126400897.1502651783.1507737812.1509991807.3",
  "__utmz": "242358273.1509991807.3.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)",
  "_ga": "GA1.2.2126400897.1502651783",
  "_gid": "GA1.2.403848991.1510155744",
  "_shibsession_63616d70757368747470733a2f2f63616d7075732e7269742e6564752f73686962626f6c657468": "_df9d842ee4aa1a3efa10bbce2f5a4be0",
  "aupodritx33-20018-PORTAL-PSJSESSIONID": "qAmcfH07WJt3If_2mXL-th6sY7sE_pq0!1303002563",
  "https%3a%2f%2fcampus.rit.edu%2fpsp%2fpritxj%2femployee%2fhrms%2frefresh": "list: %3ftab%3ddefault|%3frp%3ddefault|%3ftab%3dremoteunifieddashboard|%3frp%3dremoteunifieddashboard",
  "ps_theme": "node:HRMS portal:EMPLOYEE theme_id:DEFAULT_THEME_CLASSIC accessibility:N",
  "psback": "%22%22url%22%3A%22https%3A%2F%2Fcampus.rit.edu%2Fpsc%2FPRITXJ%2FEMPLOYEE%2FHRMS%2Fc%2FSA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL%3FPage%3DSSR_SSENRL_CART%26Action%3DA%26ACAD_CAREER%3DGRAD%26EMPLID%3D580000313%26INSTITUTION%3DRIT01%26STRM%3D2175%26TargetFrameName%3DNone%22%20%22label%22%3A%22Enrollment%3A%20%20Add%20Classes%22%20%22origin%22%3A%22PIA%22%20%22layout%22%3A%220%22%22",
  "site": "http%3A%2F%2Fist.rit.edu%2Findex.php"
}


data = {
  "ICAJAX": "1",
  "ICNAVTYPEDROPDOWN": "1",
  "ICType": "Panel",
  "ICElementNum": "0",
  "ICStateNum": "8",
  "ICAction": "DERIVED_REGFRM1_LINK_ADD_ENRL$82$",
  "ICXPos": "0",
  "ICYPos": "507",
  "ResponsetoDiffFrame": "-1",
  "TargetFrameName": "None",
  "FacetPath": "None",
  "ICFocus": "",
  "ICSaveWarningFilter": "0",
  "ICChanged": "-1",
  "ICAutoSave": "0",
  "ICResubmit": "0",
  "ICSID": "c/WzUw6t5WS79ciApq29gSYjK+tzS5cVMUj5XP/QboM=",
  "ICActionPrompt": "false",
  "ICTypeAheadID": "",
  "ICBcDomData": "C~HC_SSR_SSENRL_CART_GBL~EMPLOYEE~HRMS~SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL~UnknownValue~Enrollment:  Add Classes~UnknownValue~UnknownValue~https://campus.rit.edu/psp/PRITXJ/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL~UnknownValue*C~HC_SSS_STUDENT_CENTER~EMPLOYEE~HRMS~SA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL~UnknownValue~Student Center~UnknownValue~UnknownValue~https://campus.rit.edu/psp/PRITXJ/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSS_STUDENT_CENTER.GBL~UnknownValue*F~CO_EMPLOYEE_SELF_SERVICE~EMPLOYEE~HRMS~UnknownValue~UnknownValue~Self Service~UnknownValue~UnknownValue~https://campus.rit.edu/psp/PRITXJ/EMPLOYEE/HRMS/s/WEBLIB_PT_NAV.ISCRIPT1.FieldFormula.IScript_PT_NAV_INFRAME?pt_fname=CO_EMPLOYEE_SELF_SERVICE&c=EeUtsS8PreCN5r8jyS8L3T9HzFApegKe&FolderPath=PORTAL_ROOT_OBJECT.CO_EMPLOYEE_SELF_SERVICE&IsFolder=true~UnknownValue",
  "ICFind": "",
  "ICAddCount": "",
  "ICAPPCLSDATA": "",
  "DERIVED_SSTSNAV_SSTS_MAIN_GOTO$7$": "9999",
  "DERIVED_REGFRM1_CLASS_NBR": "",
  "DERIVED_REGFRM1_SSR_CLS_SRCH_TYPE$249$": "06",
  "DERIVED_SSTSNAV_SSTS_MAIN_GOTO$8$": "9999",
  "ptus_defaultlocalnode": "PSFT_HR",
  "ptus_dbname": "PRITXJ",
  "ptus_portal": "EMPLOYEE",
  "ptus_node": "HRMS",
  "ptus_workcenterid": "",
  "ptus_componenturl": "https://campus.rit.edu/psp/PRITXJ/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL"
}


url = "https://campus.rit.edu/psc/PRITXJ/EMPLOYEE/HRMS/c/SA_LEARNER_SERVICES.SSR_SSENRL_CART.GBL"

rep = requests.post(url, data=data, cookies=cookies, headers=headers)

rep.statuc_code