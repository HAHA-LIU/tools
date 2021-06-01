import pymysql
import uuid
import datetime

db = pymysql.connect('39.98.59.164', 'root', '@sinde123', 'dajian_old', charset='utf8')

cur = db.cursor()

sql = "SELECT * FROM dj_users WHERE role='0'"

cur.execute(sql)

result = cur.fetchall()

for i in result:
    remarks = '1'
    time_s = datetime.datetime.now()
    new_pass = ''


    if i[15]:
        time_s = i[15]
    elif i[17]:
        time_s = i[17]

    if i[25] == '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92':
        new_pass = '6a1c81fafe95cbef01b4ad0f3352c35be53dd514bb161daba67c4244'
        remarks = '0'
    elif i[25] == 'bb421fa35db885ce507b0ef5c3f23cb09c62eb378fae3641c165bdf4c0272949':
        new_pass = '8b0bcfc55265dce06363711d9678845c188ee56f8b4f7385fec8f590'
        remarks = '0'
    elif i[25] == '15e2b0d3c33891ebb0f1ef609ec419420c20e320ce94c65fbc8c3312448eb225':
        new_pass = '01a657ba8ac31d5b9219760ba26c458d7066893bd880de842671432a'
        remarks = '0'
    elif i[25] == '615ed7fb1504b0c724a296d7a69e6c7b2f9ea2c57c1d8206c5afdf392ebdfd25':
        new_pass = '638d2c6877dfa9b90a77be131008d346eaa8012837c132d47ce33404'
        remarks = '0'
    elif i[25] == '719220b3aea3ec63c7c018582c9d589045f013eb90d5e62e1b6802dfbe47f16c':
        new_pass = '60549ac904a870388b05a22bdfe0da0d1a9a864fd586567c453f534a'
        remarks = '0'
    elif i[25] == 'bfafd96c1f51c7adb8d7a69d8986648ee10f58853bbd385e3456b01cb5269665':
        new_pass = '54acf3f5064f5ff845020286cfc6350ec3bb0cd7af24ca7c13a94dc5'
        remarks = '0'
    elif i[25] == '34ae25415c5ff5375741b3d711d1cab5e522432e736631b39eb712813bf0d6d0':
        new_pass = '05c1a647358b1586af31677261b13951d425fe082cb0f65ffafacac4'
        remarks = '0'
    elif i[25] == '96a20c2f991e57d5b25247d00a2ec69e7d849bde2ebb18c27fd7862d90ba4849':
        new_pass = 'c4b9e426fe8ae13d883fd1dec02ee63cc914262f82c51fb1fc4fef34'
        remarks = '0'
    elif i[25] == '49675692d15037fecd7313e99d88b95c9366e68a7b98071858cb67a43904ca24':
        new_pass = 'c534b6622b97e3d8425d8b2df4e47e8281f82e7706d2e57344b3345a'
        remarks = '0'
    elif i[25] == '6d19ca72de1fe7973e5a763cdbaf47af34674d4f45a8a2cacd881b751d680a4f':
        new_pass = '25c5b0d4fc19e090186ac188d266d9ca28f82305237d3dc4e8372686'
        remarks = '0'
    elif i[25] == 'd60eb64310ea92a17ad0685b3f27729b2eed2241eee06dac31db9c444e52fdb0':
        new_pass = 'e057e13e0778d1d4304bb662e38049c32312fdb95f5d0387d425d516'
        remarks = '0'
    elif i[25] == '07ba38d7a9affba269a613da6d99a7ffa4d128ce38f5e24ee5a7383b796b58b2':
        new_pass = '541b909b2d75b5bb2b3ab2efd2a208fd4c4189a36b56c67d27e5bcdc'
        remarks = '0'
    elif i[25] == 'eaaf4f7e68070845a0e4afcea9cd4c622ccee7150e60e81c463fd376b060a6c9':
        new_pass = '5a0e784a134cd6f82bfafe8cd22012950e38db4b5f5525e5313231e3'
        remarks = '0'
    elif i[25] == '1fc051c04edc85344f1adb85e5abbdfd089e896b6982e9d1bcb8580267d565fb':
        new_pass = '2155e4f76dd62216718ce17ecc3438b5e89618522980ec6b5e6cf19d'
        remarks = '0'
    elif i[25] == '91b4d142823f7d20c5f08df69122de43f35f057a988d9619f6d3138485c9a203':
        new_pass = '7109c14f385ab947628e57b8eab50dc8db6026155372e40f9f418b1b'
        remarks = '0'
    elif i[25] == '2b0800ff2e3b6619b49cc8461db1fdb02870c8f7c2bc03b5012a77e15dec4c09':
        new_pass = '10a00095bb0f063fe5729c99804c8724efff74d5418e98bf7b7a9764'
        remarks = '0'
    elif i[25] == '2b250bf5a18c565360f45eca89ed4ff519c98ad5886c163b6e3c5b4a75a840f9':
        new_pass = 'c1645ba278b883a8b465a9607a0d11886ef139d99a811ca9c9a04784'
        remarks = '0'
    elif i[25] == '2594012b3453a433ffc609a6c3c79907a952471d591ddd42b7abf658b929bc5a':
        new_pass = '07ea85b4ffc9b957916b8c561fb4268eaa3a9c1df03e84acbdcddd29'
        remarks = '0'
    elif i[25] == 'f7540cffda89f137b8fb08eb5cc12806d81690e4777855c07c2ed9992bb04d82':
        new_pass = '96bc90dc52c1b832ad834040cfe47865b5685e319a33f49417c1d784'
        remarks = '0'
    elif i[25] == '77e396a4b27d903be0ca7fe3917b1563dcae3e90bcef43325d17b7b9a3e0b1c0':
        new_pass = '61404b4e467bdc1c70ca9bf8cf8ff54426d4d6e9d54fc8c879ba8875'
        remarks = '0'
    elif i[25] == '146b5bf224c840df30c1a0bc55b9b732a41b70eab4e133dfae212f9f0bcb0d6a':
        new_pass = 'f9e1619b8af1f35168e79219b894303e91add9a933467985d5a1274e'
        remarks = '0'
    elif i[25] == '40dd4b0cb6e2bef6bfe3ab8a7c1bd66d3265c5132e143f41da55635906ab2ae1':
        new_pass = '7ff1a429500b80291c4115154233c7d452b7e499bcf469db7deceb10'
        remarks = '0'
    elif i[25] == '129b80641f8b79cf1abcda58432ffdf70fd9a52b25269f731e16fd6626c3fa65':
        new_pass = '140c53f762f668d10e56709134ea773d1ea2f3b26087feab64033aab'
        remarks = '0'
    elif i[25] == '1a79416820f6f26dae2cd14674cdca3eb3c1b7bb379e13b5ea65a7da6ed40e35':
        new_pass = '5d8fe9da32f0a8065f7a0e986049f9797c2799babf6b34641f863094'
        remarks = '0'
    elif i[25] == '5e39662e1927d091bb2867baccce9e12812f6648983ad58d73114098f4b0d9df':
        new_pass = 'a54ca4e2d4980525fab767fc0fff482366a92a12d2fec51a87b787c5'
        remarks = '0'
    elif i[25] == '0b7d75c068ed5165be960279e7dacd2e900d50cbae19b654d02efc5b0fa68ee8':
        new_pass = 'd5a6744469beebfdf57be25d6d0c6a549da5cc7f150f801723060fde'
        remarks = '0'
    elif i[25] == 'c1ecace34ec13d18697f5c5c2a9e1a355ce83827ef79346d7161ca0d354808f7':
        new_pass = '1e37028738283455d9ff8ca386da987a90bc39480df22650dabb0e96'
        remarks = '0'
    elif i[25] == '092aacbb50fa3b10f2c322dca1bc1b24542afedc610f83f4dd95923f62aa4293':
        new_pass = '533bfc7d7059ae5b8d8c5414b896b2ec0bc67c22d3ecd0d5556a85bc'
        remarks = '0'
    elif i[25] == '9bfa0b50a90e669907e78780bcc1e5e972742e0d124b30a67fbeb6371c604891':
        new_pass = 'c8c9d0645b2eb78aab82a3715129c68af24ab3b86b2c7282a7a44880'
        remarks = '0'
    elif i[25] == '5600715f42bf51c40dc330d750cd996f58fead4ddea56466ce7498d17801b3a5':
        new_pass = '7883d77d27c2a3c3711fee588f6cd4e1c50291883c0e085eca5c8441'
        remarks = '0'
    elif i[25] == '47a00fac3b4c8586b401e39aaea52a887da32b78fad88a09a9839fd5af0826a2':
        new_pass = '559c38f2f13ee436ced8c82a6609ffacac6ee4e2711b0f7a14a3f89d'
        remarks = '0'
    elif i[25] == 'f641ac8e1af52421e59b43e69b478a8a8e5501b454355bfe8a9d9871924cc1b3':
        new_pass = '17db3ee06389407eb53b30b6da964947a1a58ceb8aa73711063402c1'
        remarks = '0'
    elif i[25] == '6e827e60aa721c91d74f0fd5838e135ee0b0405ccb714b3cdc22fcd8ec8dfb56':
        new_pass = '2d7286f0da0e496ed07091de936f4c1b85ed0ec559ae43ca4e0b50a1'
        remarks = '0'
    elif i[25] == 'bf9b5655b05750ddec4210c33d21fb32494fe1884d505d41ed47975a48421917':
        new_pass = 'ec733b598982d033f2fe7d80844b4979e51040f1a236fb68bf5493b3'
        remarks = '0'
    elif i[25] == '68e4150dd5853018ca89613c1a7e677daf0bf6e794ed344287ad4060a9782afd':
        new_pass = 'b3f5f86a05461d1a3f9226a24411af62f79f2ebf8d0e4ed591a7056a'
        remarks = '0'
    elif i[25] == '0fc50dbafa08ab8ff64b35e5c2b18b7016cfb525fc8c6a10ae5ba39ef51f8827':
        new_pass = '45629ac1200615502e9b4d3b2c16a328770ce9b39187effa7c05f90b'
        remarks = '0'
    elif i[25] == '322ac95422a499ac10ec18221a66102ebbad25f2d869782b787ed27cc0c96e03':
        new_pass = 'a4a9e60cbd063565f7aa95abb72212ff9f83f132cd884ed29ee594c3'
        remarks = '0'
    elif i[25] == '9a54bf37edee0c0a3a8df7414abf991f8b08048ce1ab01d0e50addb8c76840bf':
        new_pass = 'fdd758c6b9298547e5f145dfc3c9b1e0a1b6a7875bf295ff14912b4f'
        remarks = '0'
    elif i[25] == '9b4ae874674d2cce761323e40c0323eead18be7fa52f5d820a5c18803efef9da':
        new_pass = '9c088b7c6a95e4c10c4ce5dbc05dd45d6ca41b9f38a6557bdcf521b7'
        remarks = '0'
    elif i[25] == 'e4dbd4f099389c3968df91f39e7d5ae8685951f3956c13c66d15267c823eeb4f':
        new_pass = '08c1f5012dd7ec77c8efcc2309409b5037d47caf7c73e61b1c78fced'
        remarks = '0'
    elif i[25] == 'd16d557f5999563aa644d98ce27ec23d066891bda53e2f13e71fc41489602813':
        new_pass = '40dca2930ad7cdc02deff01ae966fad6d7ac18b15296d952623accb1'
        remarks = '0'
    elif i[25] == 'a03c32fcd351cba2d9738622b083bed022ef07793bd92b59faea0207653f371d':
        new_pass = '2142ea69ee6d1acb59428bbba88486749428fcfab34772488772cfe7'
        remarks = '0'
    elif i[25] == '0a57b960858f60e22de87aa6c58010ac548751fae0282345dcb13b4519e2034f':
        new_pass = '6fd2b9636802c6586bb58bca2472d59e5909618eff90221056603bb7'
        remarks = '0'
    elif i[25] == '0cf1ef7f25542152d75871f1a207e1129826886ce5d47ad7265f53dac0f943f7':
        new_pass = 'cf05b400aa90fc5bd49b82e4342ad1b42f414a29bbb3db10ae3a5dc5'
        remarks = '0'
    elif i[25] == '818183fd88dcb41d12bcba416794d2cbaf4aec9a1b10deb580b514a339c9a8d1':
        new_pass = 'a55c08b7bb4e468cb4ea298643f0d536b8655e267750898395140686'
        remarks = '0'
    elif i[25] == '38ebf6eca9ce750f2f4eb131e9c1c9177220500a73b08044345ecf0c7d02d780':
        new_pass = '23a986990790ac267479807fed49070e0b1d1ae1f37b6c342fa7b6d1'
        remarks = '0'
    elif i[25] == '6ea8a4334424228d77429bf5ab529a4fab929ea6e69fbaa4c9cefc5c66fe89e0':
        new_pass = '82d115526037324d1ffd93c99db115c49b4222ba91ca818cff059089'
        remarks = '0'
    elif i[25] == '77788009d81e1dce3a0ffc93c9ef91360f56f40a54182fc25c99c6309a2eae7b':
        new_pass = '419d4c4b78e2ccdd4962f0b5d4c65e35a468c47e697f56682c74839e'
        remarks = '0'
    elif i[25] == '112cd1678fbb4ceab507e9a2df3d1b213dd5b8d85fa93f56c2601b92a3b3e11f':
        new_pass = '6a3a296e93dd1304f96f5439e305021a9b2c114be72944633ab8a6e3'
        remarks = '0'
    elif i[25] == '82aac7818a5f7e648855e016bd87315100e5c968c5aa0c4a035b5ecb65a23b95':
        new_pass = '7f99b311fae052887711e5735d83f4c80a8cbb5d9957c6142cacb914'
        remarks = '0'
    elif i[25] == 'cfb789f892fdf2a45ab1bc1f046932df431a7708165393e0f13fab2c9267c0eb':
        new_pass = '910f70a0db4c85b017e716389a84877d089d781a527cbff47ba41ca8'
        remarks = '0'
    elif i[25] == '4f47c6e346e2ed8f7bbd3a999f6cd143fc8af137161a64f7ca9534686a95f6d2':
        new_pass = '0ac5d289372ac4187241ced7b8f6b516ab9a8dab74acae8222455a78'
        remarks = '0'
    elif i[25] == '71343abc970a5dec1074584d9f0cc4daa0b0c30303a241d0546c6fee1f789976':
        new_pass = '7435af15081b84690e08f6aefd676f15d08714e855046a54414f7ddc'
        remarks = '0'
    elif i[25] == '8a9bcf1e51e812d0af8465a8dbcc9f741064bf0af3b3d08e6b0246437c19f7fb':
        new_pass = '98c1a1a3a448e1221a098af6c584c4dd1e3c1afba1178fcf9d144716'
        remarks = '0'
    elif i[25] == '00b2be8283dd61b23b57f6a6eac7c2ae18496907d517d0418e95cb15f1e5b1d9':
        new_pass = '9262e65055fea3caf1d5030b610d1504fe4032b808ec8ebebff52013'
        remarks = '0'
    elif i[25] == 'da15ee0f89baab42cc3e31c5684c29ca802b57e6d2579fa186470329180cad43':
        new_pass = 'c21247b78122a076b44369b086cfe6e25abdf184b8332580b7274e18'
        remarks = '0'
    elif i[25] == '9d60b87fba8796224e0f9b025fd99cb75951e8a69bfaaaafcda4292b88c27282':
        new_pass = '5b3d220307078c81f5f94cb5c0c258e6574406e95c9d1bf5bd425e1b'
        remarks = '0'
    elif i[25] == 'd70ee372f020159528f43254b96dfaf89b99c060fee862e13c1c2a894d79897b':
        new_pass = 'b94ae25ead235549b963cf076523e01a4e432691581b222b8b6c23d9'
        remarks = '0'
    elif i[25] == 'a0d2b5491417210912c83c9edce9a3e2395480d7acf05377285d2b4a4ade08d9':
        new_pass = 'd13224b91ffa2d051c18e2cfcecdd53ecc8b75a36358647deaab4ef2'
        remarks = '0'
    elif i[25] == '52bb588ddc390e0dd995855cf95c2c75029410728890a535e8aef70fc4df91f4':
        new_pass = '7ba954d539b9d601ddef33bb1ad5e519ef7a2cb22ecffd205d2d3c75'
        remarks = '0'
    elif i[25] == 'e3f427ebfe0c364ff8d81594af0fdfd484d3964d52bdd458b3268f8246db3f3b':
        new_pass = 'a1606ea5a6370bc4dcd486e074547e45b89f055d38c16fc9e0ab7b4d'
        remarks = '0'
    elif i[25] == '29b8aebd2c6bad9452a5dffd503a716ac71a2d48f34d59d1ab84548d4cb05fe7':
        new_pass = 'e91f151af0b84a2f40628d6a3897cbd07491d98ff35be03cf41058e3'
        remarks = '0'
    elif i[25] == 'db418e6299b87ea285cf659c1b131726eb93dcaab8b544a0a15d9137c29708d8':
        new_pass = '61e6cd9381e0011ca089cd7fea8fbdc8cd198794d759eeb214161f52'
        remarks = '0'
    elif i[25] == '80916973036c3af16c6bd4e38b1229cdfb096884704fa1bbaa7dd97d8017629b':
        new_pass = 'a3a484cc878b736eae9f046d9d460463efd52dee3caebf5b739909ac'
        remarks = '0'


    # 插入基础用户信息表
    sql2 = "insert into `bf-db2`.sys_user(id,open_id,login_name,password,mobile,user_type,active_flag,auth_flag,login_flag," \
       "create_date,remarks,del_flag) values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(i[0],str(uuid.uuid4()).replace('-',''),i[1],new_pass,i[3],'1','1','1','1',time_s,remarks,'0')
    cur.execute(sql2)

    # 插入用户角色关系表
    sql3 = "insert into `bf-db2`.sys_user_role values ('{}','{}'),('{}','{}')".format(i[0],'0',i[0],'2')
    cur.execute(sql3)

    other_name = i[4]
    if other_name == '未设置':
        other_name = '用户'+i[3][-4:]

    # 插入用户拓展表
    sql4 = "insert into `trade-info2`.info_user_message(id,user_id,nick_name,phone,from_type,del_flag," \
           "create_date,remarks) values ('{}','{}','{}','{}','{}','{}','{}','{}')".format(str(uuid.uuid4()).replace('-',''),
        i[0],other_name,i[3],'1','0',time_s,remarks)
    cur.execute(sql4)

db.commit()



