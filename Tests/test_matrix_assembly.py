import os
import subprocess
import unittest
from BSB.BSB_Matrix.MatrixAggregator import AggregateMatrix
from BSB.BSB_Impute.Impute_Utils.ImputationFunctions import get_bsb_matrix

# get current directory

test_directory = os.path.dirname(os.path.realpath(__file__))
bsb_directory = '/'.join(test_directory.split('/')[:-1]) + '/'
bsbolt = f'{bsb_directory}BSBolt.py'

test_cgmap_file = [f'{test_directory}/TestData/test_cgmap_files/1.cgmap.gz',
                   f'{test_directory}/TestData/test_cgmap_files/2.cgmap',
                   f'{test_directory}/TestData/test_cgmap_files/3.cgmap',
                   f'{test_directory}/TestData/test_cgmap_files/4.cgmap']

# missing and low count sites
val_sites = ['chr14:3687', 'chr14:4105', 'chr14:4428', 'chr14:5629', 'chr14:5700', 'chr14:5792', 'chr14:6480',
             'chr14:6527', 'chr14:6833', 'chr14:6938', 'chr14:8932', 'chr14:8965', 'chr12:303', 'chr12:641',
             'chr12:1991', 'chr12:3966', 'chr12:5287', 'chr12:8552', 'chr13:4940', 'chr13:4985', 'chr13:5123',
             'chr13:5844', 'chr13:5851', 'chr13:9432', 'chr13:9970', 'chr11:828', 'chr11:910', 'chr11:1048',
             'chr11:1669', 'chr11:2812', 'chr11:3166', 'chr11:3941', 'chr11:4003', 'chr11:4741', 'chr11:5456',
             'chr11:8497', 'chr10:1707', 'chr10:2933', 'chr10:3333', 'chr10:4978', 'chr10:5374', 'chr10:5413',
             'chr10:5770', 'chr10:9751', 'chr10:9782', 'chr14:10225', 'chr14:10433', 'chr14:11280', 'chr14:11726',
             'chr14:11929', 'chr14:13704', 'chr14:13984', 'chr14:14280', 'chr14:15090', 'chr14:18019', 'chr12:10951',
             'chr12:16254', 'chr12:17203', 'chr12:17301', 'chr12:17462', 'chr12:17707', 'chr12:17801', 'chr12:18828',
             'chr10:10622', 'chr10:10904', 'chr10:12028', 'chr10:13869', 'chr10:14137', 'chr10:14176', 'chr10:14414',
             'chr10:14952', 'chr10:15081', 'chr10:15765', 'chr13:10424', 'chr13:11792', 'chr13:13306', 'chr13:13849',
             'chr13:14740', 'chr13:15221', 'chr13:17141', 'chr13:17328', 'chr13:18949', 'chr13:18964', 'chr11:10113',
             'chr11:10636', 'chr11:12686', 'chr11:14791', 'chr11:15011', 'chr11:15559', 'chr11:15761', 'chr11:16829',
             'chr11:18076', 'chr11:18212', 'chr11:18939', 'chr11:19707', 'chr12:20359', 'chr12:23401', 'chr12:24050',
             'chr12:24361', 'chr12:24643', 'chr12:25561', 'chr12:27835', 'chr11:21763', 'chr11:21883', 'chr11:22773',
             'chr11:23812', 'chr11:24393', 'chr11:24782', 'chr11:24812', 'chr14:21424', 'chr14:21930', 'chr14:22423',
             'chr14:23792', 'chr14:25522', 'chr14:25987', 'chr14:26621', 'chr14:28415', 'chr10:20272', 'chr10:20304',
             'chr10:22113', 'chr10:22986', 'chr10:23984', 'chr10:24416', 'chr10:25052', 'chr10:25451', 'chr10:27473',
             'chr10:27885', 'chr10:29240', 'chr10:29668', 'chr13:20446', 'chr13:21084', 'chr13:21302', 'chr13:23115',
             'chr13:24127', 'chr13:25036', 'chr13:26028', 'chr13:27223', 'chr13:27888', 'chr13:28182', 'chr13:29431',
             'chr14:30698', 'chr14:31925', 'chr14:33481', 'chr14:33771', 'chr14:33774', 'chr14:34584', 'chr14:36460',
             'chr14:38452', 'chr14:38488', 'chr10:32432', 'chr10:34065', 'chr10:34448', 'chr10:37669', 'chr10:38544',
             'chr11:31777', 'chr11:34851', 'chr11:35725', 'chr11:36364', 'chr11:36741', 'chr11:37085', 'chr11:37525',
             'chr11:37921', 'chr11:39117', 'chr11:39125', 'chr11:39533', 'chr12:30356', 'chr12:31008', 'chr12:36079',
             'chr12:36710', 'chr12:38967', 'chr12:39072', 'chr13:30432', 'chr13:34692', 'chr13:35973', 'chr13:36693',
             'chr13:37660', 'chr13:37890', 'chr13:38363', 'chr13:39269', 'chr13:39761', 'chr11:41063', 'chr11:42080',
             'chr11:45261', 'chr11:45351', 'chr11:45745', 'chr11:46734', 'chr11:46878', 'chr11:47080', 'chr11:48335',
             'chr11:48398', 'chr11:48989', 'chr11:49621', 'chr14:40645', 'chr14:41309', 'chr14:41408', 'chr14:41784',
             'chr14:42710', 'chr14:43344', 'chr14:44812', 'chr14:46708', 'chr14:46770', 'chr14:46954', 'chr14:47024',
             'chr14:48750', 'chr14:49011', 'chr14:49784', 'chr10:44116', 'chr10:44344', 'chr10:44611', 'chr10:48652',
             'chr10:48672', 'chr10:48710', 'chr13:41646', 'chr13:42041', 'chr13:44570', 'chr13:44576', 'chr13:45683',
             'chr13:45781', 'chr13:48639', 'chr13:48738', 'chr12:42120', 'chr12:43031', 'chr12:43470', 'chr12:43769',
             'chr12:44525', 'chr12:46112', 'chr12:46288', 'chr12:47151', 'chr12:47426', 'chr12:47868', 'chr12:49644',
             'chr12:49839', 'chr11:50123', 'chr11:51463', 'chr11:51474', 'chr11:51572', 'chr11:52362', 'chr11:52380',
             'chr11:53922', 'chr11:54002', 'chr11:54995', 'chr11:55675', 'chr11:56385', 'chr11:57709', 'chr11:57858',
             'chr10:52029', 'chr10:52463', 'chr10:52895', 'chr10:54130', 'chr10:54724', 'chr10:54968', 'chr10:57302',
             'chr10:57467', 'chr10:57842', 'chr10:58398', 'chr14:53655', 'chr14:53664', 'chr14:54765', 'chr14:56172',
             'chr14:56492', 'chr14:58193', 'chr14:58879', 'chr12:50820', 'chr12:50839', 'chr12:50892', 'chr12:53114',
             'chr12:54112', 'chr12:54923', 'chr12:55377', 'chr12:55997', 'chr12:56301', 'chr12:57179', 'chr12:57501',
             'chr13:51005', 'chr13:52285', 'chr13:52729', 'chr13:52738', 'chr13:55106', 'chr13:55755', 'chr13:56381',
             'chr13:58060', 'chr13:59021', 'chr10:60053', 'chr10:61476', 'chr10:62963', 'chr10:63630', 'chr10:64505',
             'chr10:64643', 'chr10:65660', 'chr10:65835', 'chr10:66458', 'chr10:66634', 'chr10:67221', 'chr11:61645',
             'chr11:62492', 'chr11:62548', 'chr11:62597', 'chr11:62807', 'chr11:62902', 'chr11:63098', 'chr11:63458',
             'chr11:64565', 'chr11:64746', 'chr11:65482', 'chr11:66074', 'chr11:66478', 'chr11:68666', 'chr14:60095',
             'chr14:60355', 'chr14:63198', 'chr14:64716', 'chr14:64770', 'chr14:67343', 'chr14:67440', 'chr14:68109',
             'chr14:69764', 'chr12:60969', 'chr12:61942', 'chr12:62476', 'chr12:64732', 'chr12:65058', 'chr12:65259',
             'chr12:65641', 'chr12:66095', 'chr12:69793', 'chr13:61004', 'chr13:61225', 'chr13:64828', 'chr13:64956',
             'chr13:64983', 'chr13:65763', 'chr13:66986', 'chr13:69537', 'chr10:72317', 'chr10:72946', 'chr10:73933',
             'chr10:75421', 'chr10:75488', 'chr10:75840', 'chr10:76041', 'chr10:76178', 'chr10:76270', 'chr10:76640',
             'chr10:77881', 'chr10:77887', 'chr10:78696', 'chr10:78937', 'chr14:73659', 'chr14:73840', 'chr14:75296',
             'chr14:76219', 'chr14:78050', 'chr14:79013', 'chr14:79401', 'chr12:73700', 'chr12:74836', 'chr12:75067',
             'chr12:75739', 'chr12:75752', 'chr12:76429', 'chr12:76805', 'chr12:76839', 'chr12:77073', 'chr12:77594',
             'chr12:77822', 'chr12:77887', 'chr12:78063', 'chr12:79716', 'chr11:70492', 'chr11:72644', 'chr11:76423',
             'chr11:76990', 'chr11:77574', 'chr11:77771', 'chr11:78864', 'chr11:79660', 'chr11:79820', 'chr13:70119',
             'chr13:71836', 'chr13:73974', 'chr13:74641', 'chr13:74811', 'chr13:75567', 'chr13:75829', 'chr13:76579',
             'chr13:78027', 'chr13:78807', 'chr12:81587', 'chr12:81816', 'chr12:81972', 'chr12:82629', 'chr12:82643',
             'chr12:83140', 'chr12:83565', 'chr12:84144', 'chr12:86536', 'chr12:88568', 'chr12:89587', 'chr10:81386',
             'chr10:81866', 'chr10:82299', 'chr10:82751', 'chr10:83373', 'chr10:83758', 'chr10:84895', 'chr10:85268',
             'chr10:85570', 'chr10:86442', 'chr10:86869', 'chr10:88072', 'chr10:88827', 'chr14:82135', 'chr14:82419',
             'chr14:82704', 'chr14:82725', 'chr14:82976', 'chr14:83427', 'chr14:83688', 'chr14:84623', 'chr14:88403',
             'chr13:81636', 'chr13:83031', 'chr13:83741', 'chr13:83954', 'chr13:84630', 'chr13:84940', 'chr13:85152',
             'chr13:85156', 'chr13:85648', 'chr13:85673', 'chr11:80846', 'chr11:81704', 'chr11:82047', 'chr11:82349',
             'chr11:82498', 'chr11:83860', 'chr11:87172', 'chr11:87836', 'chr11:88491', 'chr10:90074', 'chr10:90649',
             'chr10:90916', 'chr10:91301', 'chr10:93701', 'chr10:94551', 'chr10:95460', 'chr10:95737', 'chr10:97545',
             'chr10:97564', 'chr10:98769', 'chr10:99661', 'chr12:92759', 'chr12:93773', 'chr12:94265', 'chr12:95176',
             'chr12:96431', 'chr12:96937', 'chr12:97692', 'chr12:98416', 'chr12:98540', 'chr13:92077', 'chr13:92651',
             'chr13:96362', 'chr14:91079', 'chr14:91615', 'chr14:92423', 'chr14:92460', 'chr14:93822', 'chr14:95633',
             'chr14:96655', 'chr14:96866', 'chr14:97810', 'chr14:99069', 'chr14:99327', 'chr14:99521', 'chr11:91016',
             'chr11:91627', 'chr11:92637', 'chr11:92817', 'chr11:94008', 'chr11:94215', 'chr11:94399', 'chr11:94843',
             'chr11:96387', 'chr11:96835', 'chr12:100250', 'chr12:100855', 'chr12:100891', 'chr12:101702',
             'chr12:103931', 'chr12:105253', 'chr12:105696', 'chr12:105739', 'chr12:106005', 'chr12:106007',
             'chr12:106022', 'chr12:107405', 'chr12:107737', 'chr12:108074', 'chr12:108281', 'chr12:108425',
             'chr12:109695', 'chr12:109860', 'chr10:100501', 'chr10:101190', 'chr10:101396', 'chr10:102285',
             'chr10:103140', 'chr10:103533', 'chr10:105111', 'chr10:106175', 'chr10:106922', 'chr10:108365',
             'chr10:109866', 'chr11:102354', 'chr11:103163', 'chr11:103714', 'chr11:103860', 'chr11:105206',
             'chr11:107183', 'chr11:108166', 'chr11:108399', 'chr14:100924', 'chr14:101039', 'chr14:102394',
             'chr14:102556', 'chr14:102987', 'chr14:103884', 'chr14:104521', 'chr14:105460', 'chr14:105663',
             'chr14:105746', 'chr14:107803', 'chr14:107977', 'chr14:108279', 'chr14:108294', 'chr14:108943',
             'chr14:109907', 'chr13:100867', 'chr13:102129', 'chr13:102154', 'chr13:104860', 'chr13:105155',
             'chr13:105156', 'chr13:105439', 'chr13:105447', 'chr13:105717', 'chr13:108892', 'chr13:109017',
             'chr13:109663', 'chr13:109697', 'chr11:110564', 'chr11:110661', 'chr11:111623', 'chr11:112355',
             'chr11:113387', 'chr11:114069', 'chr11:114354', 'chr11:114649', 'chr11:114893', 'chr11:115021',
             'chr12:110039', 'chr12:110082', 'chr12:110897', 'chr12:111778', 'chr12:113156', 'chr12:114021',
             'chr12:114533', 'chr12:114597', 'chr12:116640', 'chr12:118629', 'chr12:119156', 'chr10:110095',
             'chr10:110780', 'chr10:110859', 'chr10:111776', 'chr10:112843', 'chr10:113939', 'chr10:114620',
             'chr10:114992', 'chr10:115207', 'chr10:115334', 'chr10:115892', 'chr10:117259', 'chr10:117532',
             'chr10:117635', 'chr10:117875', 'chr10:119295', 'chr14:110183', 'chr14:111397', 'chr14:112141',
             'chr14:112483', 'chr14:112896', 'chr14:113481', 'chr14:113538', 'chr14:113610', 'chr14:114707',
             'chr14:116920', 'chr14:117870', 'chr14:118226', 'chr14:118794', 'chr14:119214', 'chr14:119314',
             'chr14:119339', 'chr14:119440', 'chr13:112427', 'chr13:113690', 'chr13:114276', 'chr13:114599',
             'chr13:116557', 'chr13:116983', 'chr13:117063', 'chr13:117122', 'chr13:117260', 'chr13:118131',
             'chr13:118182', 'chr13:118826', 'chr11:122491', 'chr11:122567', 'chr11:125533', 'chr11:125788',
             'chr11:127445', 'chr11:129166', 'chr11:129717', 'chr11:129994', 'chr10:120548', 'chr10:120690',
             'chr10:122433', 'chr10:123981', 'chr10:124924', 'chr10:125215', 'chr10:127430', 'chr10:127607',
             'chr10:128961', 'chr12:120278', 'chr12:120382', 'chr12:120699', 'chr12:120834', 'chr12:121048',
             'chr12:121156', 'chr12:121799', 'chr12:121834', 'chr12:123558', 'chr12:123866', 'chr12:124034',
             'chr12:125697', 'chr12:125997', 'chr12:126428', 'chr12:126834', 'chr12:126919', 'chr14:122046',
             'chr14:122609', 'chr14:125926', 'chr14:127883', 'chr14:129864', 'chr13:120778', 'chr13:121000',
             'chr13:122083', 'chr13:122782', 'chr13:123361', 'chr13:123536', 'chr13:124307', 'chr13:125235',
             'chr13:127498', 'chr13:127858', 'chr13:128715', 'chr13:129828', 'chr13:129839', 'chr11:130828',
             'chr11:132519', 'chr11:133067', 'chr11:133415', 'chr11:134437', 'chr11:134535', 'chr11:137005',
             'chr11:139282', 'chr11:139736', 'chr14:130107', 'chr14:130474', 'chr14:131403', 'chr14:132968',
             'chr14:133243', 'chr14:134377', 'chr14:135146', 'chr14:138142', 'chr14:139705', 'chr10:130583',
             'chr10:131173', 'chr10:132141', 'chr10:135434', 'chr10:137303', 'chr10:137451', 'chr10:137550',
             'chr10:138288', 'chr10:138292', 'chr12:130666', 'chr12:131038', 'chr12:131274', 'chr12:131316',
             'chr12:132687', 'chr12:133273', 'chr12:133784', 'chr12:135826', 'chr12:136923', 'chr12:136946',
             'chr12:137663', 'chr12:137904', 'chr12:138882', 'chr12:139027', 'chr12:139680', 'chr12:139729',
             'chr13:130267', 'chr13:130532', 'chr13:130592', 'chr13:132219', 'chr13:132490', 'chr13:136460',
             'chr13:137813', 'chr13:138433', 'chr13:139412', 'chr11:141163', 'chr11:141835', 'chr11:142466',
             'chr11:143953', 'chr11:144742', 'chr11:145099', 'chr11:147116', 'chr11:147124', 'chr11:147235',
             'chr11:148689', 'chr11:148849', 'chr11:149733', 'chr10:140552', 'chr10:142242', 'chr10:145924',
             'chr10:149133', 'chr10:149260', 'chr14:140885', 'chr14:143171', 'chr14:143413', 'chr14:144349',
             'chr14:145710', 'chr14:145873', 'chr14:146095', 'chr14:146757', 'chr14:148324', 'chr14:148565',
             'chr12:141649', 'chr12:141662', 'chr12:141728', 'chr12:142737', 'chr12:143512', 'chr12:143546',
             'chr12:145333', 'chr12:145419', 'chr12:146058', 'chr12:147374', 'chr12:148484', 'chr13:140302',
             'chr13:140415', 'chr13:140785', 'chr13:142108', 'chr13:142350', 'chr13:142913', 'chr13:143200',
             'chr13:143227', 'chr13:145551', 'chr13:145972', 'chr13:146010', 'chr11:150115', 'chr11:151027',
             'chr11:151068', 'chr11:151699', 'chr11:151998', 'chr11:152008', 'chr11:152337', 'chr11:152638',
             'chr11:153494', 'chr11:154401', 'chr11:154796', 'chr11:154888', 'chr11:157580', 'chr11:157625',
             'chr11:158167', 'chr11:158178', 'chr14:150411', 'chr14:154918', 'chr14:156686', 'chr14:157744',
             'chr14:159357', 'chr14:159590', 'chr10:150308', 'chr10:151619', 'chr10:152077', 'chr10:152307',
             'chr10:152715', 'chr10:153125', 'chr10:154719', 'chr10:155228', 'chr10:156179', 'chr10:156608',
             'chr10:159626', 'chr13:150582', 'chr13:151281', 'chr13:152822', 'chr13:157420', 'chr13:157986',
             'chr12:151313', 'chr12:151597', 'chr12:151982', 'chr12:153208', 'chr12:154333', 'chr12:154414',
             'chr12:154640', 'chr12:156464', 'chr12:156746', 'chr12:156784', 'chr12:157983', 'chr12:159646',
             'chr12:159813', 'chr11:160682', 'chr11:160980', 'chr11:161441', 'chr11:161511', 'chr11:162149',
             'chr11:162374', 'chr11:163454', 'chr11:167487', 'chr11:169706', 'chr14:160982', 'chr14:161944',
             'chr14:162311', 'chr14:163284', 'chr14:163478', 'chr14:163483', 'chr14:164607', 'chr14:165312',
             'chr14:165463', 'chr14:166246', 'chr14:166381', 'chr14:167398', 'chr14:167779', 'chr14:167872',
             'chr14:168258', 'chr14:168479', 'chr13:160656', 'chr13:160657', 'chr13:162341', 'chr13:162349',
             'chr13:163271', 'chr13:163371', 'chr13:164305', 'chr13:164591', 'chr13:169310', 'chr10:160998',
             'chr10:161371', 'chr10:162072', 'chr10:162094', 'chr10:162455', 'chr10:163565', 'chr10:163820',
             'chr10:165525', 'chr10:167938', 'chr10:168613', 'chr10:169342', 'chr10:169563', 'chr10:169918',
             'chr12:163405', 'chr12:163916', 'chr12:166597', 'chr12:168026', 'chr12:168535', 'chr12:168565',
             'chr11:170119', 'chr11:170243', 'chr11:170420', 'chr11:171473', 'chr11:171732', 'chr11:173259',
             'chr11:174599', 'chr11:175806', 'chr11:175904', 'chr11:177000', 'chr11:178897', 'chr11:179070',
             'chr14:172419', 'chr14:172797', 'chr14:173575', 'chr14:173770', 'chr14:173992', 'chr14:174185',
             'chr14:176482', 'chr14:178946', 'chr14:179107', 'chr10:172332', 'chr10:172846', 'chr10:173361',
             'chr10:173509', 'chr10:175406', 'chr10:176642', 'chr10:176789', 'chr10:176857', 'chr10:177765',
             'chr10:178398', 'chr10:178800', 'chr10:178855', 'chr10:179777', 'chr12:171084', 'chr12:171133',
             'chr12:171590', 'chr12:172798', 'chr12:173393', 'chr12:173672', 'chr12:174114', 'chr12:176176',
             'chr12:177493', 'chr12:179282', 'chr12:179910', 'chr13:170031', 'chr13:170382', 'chr13:170627',
             'chr13:171289', 'chr13:171984', 'chr13:172614', 'chr13:173031', 'chr13:174136', 'chr13:174794',
             'chr13:174829', 'chr13:174910', 'chr13:175413', 'chr13:175990', 'chr13:176212', 'chr13:176484',
             'chr13:178226', 'chr13:178856', 'chr13:179375', 'chr11:180133', 'chr11:180135', 'chr11:182681',
             'chr11:183132', 'chr11:183882', 'chr11:185514', 'chr11:186614', 'chr11:187053', 'chr11:187194',
             'chr11:187575', 'chr11:187608', 'chr11:188570', 'chr11:189609', 'chr11:189716', 'chr14:180796',
             'chr14:182777', 'chr14:182784', 'chr14:182971', 'chr14:186961', 'chr14:187874', 'chr14:188389',
             'chr14:189184', 'chr10:180182', 'chr10:180554', 'chr10:182376', 'chr10:183500', 'chr10:184202',
             'chr10:185502', 'chr10:186830', 'chr10:187095', 'chr10:187147', 'chr12:180002', 'chr12:181290',
             'chr12:182108', 'chr12:185948', 'chr12:187302', 'chr12:187500', 'chr12:188218', 'chr12:188687',
             'chr13:180848', 'chr13:181655', 'chr13:182497', 'chr13:183830', 'chr13:184057', 'chr13:184812',
             'chr13:185461', 'chr13:186509', 'chr13:188201', 'chr13:188401', 'chr11:193433', 'chr11:195915',
             'chr11:196654', 'chr11:197936', 'chr14:190434', 'chr14:190797', 'chr14:190994', 'chr14:193049',
             'chr14:193110', 'chr14:197037', 'chr14:197271', 'chr14:197285', 'chr14:197641', 'chr14:197858',
             'chr12:190876', 'chr12:191081', 'chr12:191102', 'chr12:193007', 'chr12:193050', 'chr12:195212',
             'chr12:196235', 'chr12:197864', 'chr12:197905', 'chr13:192283', 'chr13:192833', 'chr13:193040',
             'chr13:193525', 'chr13:193638', 'chr13:194280', 'chr13:194424', 'chr13:194472', 'chr13:194563',
             'chr13:197081', 'chr13:198128', 'chr10:192085', 'chr10:194843', 'chr10:196997', 'chr10:198248',
             'chr10:199891', 'chr10:199975', 'chr11:200884', 'chr11:202203', 'chr11:202229', 'chr11:202812',
             'chr11:203756', 'chr11:204985', 'chr11:205797', 'chr11:206511', 'chr11:206570', 'chr11:206927',
             'chr11:207722', 'chr11:207761', 'chr11:207955', 'chr11:209140', 'chr14:201322', 'chr14:201792',
             'chr14:202317', 'chr14:202630', 'chr14:204799', 'chr14:206003', 'chr14:206903', 'chr14:207270',
             'chr12:200040', 'chr12:200200', 'chr12:201293', 'chr12:203065', 'chr12:206314', 'chr12:206470',
             'chr12:207474', 'chr12:208270', 'chr13:200162', 'chr13:200591', 'chr13:200911', 'chr13:201579',
             'chr13:207176', 'chr13:207970', 'chr13:208613', 'chr13:208920', 'chr13:209671', 'chr13:209838',
             'chr10:201841', 'chr10:202356', 'chr10:205900', 'chr10:207164', 'chr10:209551', 'chr10:209882',
             'chr11:210279', 'chr11:210537', 'chr11:213580', 'chr11:214294', 'chr11:214370', 'chr11:216570',
             'chr11:216995', 'chr11:217384', 'chr11:217387', 'chr11:217704', 'chr11:218522', 'chr11:219423',
             'chr14:212768', 'chr14:215969', 'chr14:216195', 'chr14:216502', 'chr14:216890', 'chr14:217130',
             'chr14:219595', 'chr12:211045', 'chr12:212830', 'chr12:214536', 'chr12:215087', 'chr12:215476',
             'chr12:217719', 'chr12:217848', 'chr12:218145', 'chr12:219062', 'chr12:219306', 'chr12:219485',
             'chr13:210269', 'chr13:210495', 'chr13:212157', 'chr13:214009', 'chr13:215269', 'chr13:217107',
             'chr10:210492', 'chr10:211477', 'chr10:211585', 'chr10:211963', 'chr10:212321', 'chr10:213429',
             'chr10:213673', 'chr10:214096', 'chr10:214778', 'chr10:214963', 'chr10:215008', 'chr10:215022',
             'chr10:216008', 'chr10:216185', 'chr10:216246', 'chr10:216272', 'chr10:216301', 'chr10:216470',
             'chr10:217725', 'chr10:217736', 'chr10:217760', 'chr10:217885', 'chr10:219641', 'chr11:220351',
             'chr11:220836', 'chr11:221314', 'chr11:227262', 'chr14:221149', 'chr14:225428', 'chr12:220104',
             'chr12:220119', 'chr12:220217', 'chr12:221336', 'chr12:223629', 'chr12:224308', 'chr12:224954',
             'chr12:226312', 'chr12:226456', 'chr12:228225', 'chr12:228337', 'chr12:229679', 'chr12:229935',
             'chr13:223699', 'chr13:225589', 'chr13:226527', 'chr13:226710', 'chr13:226718', 'chr13:228605',
             'chr10:220234', 'chr10:220345', 'chr10:220700', 'chr10:222368', 'chr10:222915', 'chr10:223415',
             'chr10:227091', 'chr10:227120', 'chr10:229445', 'chr10:229622', 'chr14:230529', 'chr14:235974',
             'chr14:236480', 'chr14:238365', 'chr14:238581', 'chr14:238754', 'chr11:230826', 'chr11:230894',
             'chr11:231492', 'chr11:232547', 'chr11:233409', 'chr11:233762', 'chr11:234156', 'chr11:235228',
             'chr11:235811', 'chr11:237507', 'chr11:239239', 'chr12:230676', 'chr12:230810', 'chr12:231123',
             'chr12:231145', 'chr12:231325', 'chr12:231336', 'chr12:233074', 'chr12:233272', 'chr12:234199',
             'chr12:235209', 'chr12:236560', 'chr12:239189', 'chr13:231323', 'chr13:231816', 'chr13:232528',
             'chr13:232778', 'chr13:233192', 'chr13:234819', 'chr13:235125', 'chr13:236077', 'chr13:236092',
             'chr13:237772', 'chr13:237801', 'chr13:238472', 'chr10:230207', 'chr10:230211', 'chr10:230504',
             'chr10:233575', 'chr10:234300', 'chr10:237009', 'chr10:237202', 'chr10:237340', 'chr10:239534',
             'chr10:239875', 'chr14:240287', 'chr14:241639', 'chr14:242672', 'chr14:244214', 'chr14:244550',
             'chr14:244617', 'chr14:246607', 'chr14:247194', 'chr14:247296', 'chr14:247606', 'chr14:247996',
             'chr14:248851', 'chr14:249475', 'chr11:246908', 'chr11:246910', 'chr11:247231', 'chr11:247935',
             'chr11:248357', 'chr12:240368', 'chr12:243423', 'chr12:244636', 'chr12:244883', 'chr12:244954',
             'chr12:246007', 'chr12:246423', 'chr12:247979', 'chr12:248038', 'chr12:248079', 'chr12:248599',
             'chr13:240485', 'chr13:241873', 'chr13:242009', 'chr13:242150', 'chr13:242349', 'chr13:242504',
             'chr13:242554', 'chr13:243030', 'chr13:244653', 'chr13:244676', 'chr13:245507', 'chr13:247310',
             'chr13:247631', 'chr13:247693', 'chr10:239983', 'chr10:240810', 'chr10:240831', 'chr10:242139',
             'chr10:242217', 'chr10:242465', 'chr10:244470', 'chr10:244530', 'chr10:244870', 'chr10:245505',
             'chr10:245514', 'chr10:245737', 'chr10:246320', 'chr10:247229', 'chr10:248644', 'chr10:249566',
             'chr11:251039', 'chr11:251207', 'chr11:252478', 'chr11:253615', 'chr11:253617', 'chr11:253905',
             'chr11:257235', 'chr11:257503', 'chr11:257950', 'chr11:258264', 'chr11:259811', 'chr12:250081',
             'chr12:254611', 'chr12:255195', 'chr12:256734', 'chr12:256917', 'chr12:256998', 'chr12:257717',
             'chr14:251112', 'chr14:251284', 'chr14:254013', 'chr14:255514', 'chr14:256182', 'chr14:257413',
             'chr14:257451', 'chr14:258074', 'chr14:258686', 'chr13:250423', 'chr13:250491', 'chr13:252724',
             'chr13:255505', 'chr13:256374', 'chr13:256467', 'chr13:257767', 'chr13:258138', 'chr13:258364',
             'chr10:250929', 'chr10:251630', 'chr10:252392', 'chr10:253063', 'chr10:255912', 'chr10:256199',
             'chr10:256349', 'chr10:256482', 'chr10:257308', 'chr10:257558', 'chr10:259108', 'chr10:259547',
             'chr11:261237', 'chr11:261456', 'chr11:262767', 'chr11:263544', 'chr11:263582', 'chr11:265213',
             'chr11:265725', 'chr11:266782', 'chr11:268008', 'chr11:268646', 'chr11:269756', 'chr14:260026',
             'chr14:260659', 'chr14:260894', 'chr14:262108', 'chr14:262850', 'chr14:263665', 'chr14:263690',
             'chr14:264302', 'chr14:267359', 'chr14:268517', 'chr14:268945', 'chr14:269246', 'chr12:260254',
             'chr12:260771', 'chr12:262888', 'chr12:263321', 'chr12:263698', 'chr12:263968', 'chr12:264914',
             'chr12:265841', 'chr12:266719', 'chr12:267170', 'chr12:268882', 'chr13:260499', 'chr13:262379',
             'chr13:266226', 'chr13:266384', 'chr13:267491', 'chr13:268330', 'chr13:268490', 'chr13:268814',
             'chr10:260515', 'chr10:261995', 'chr10:263938', 'chr10:264734', 'chr10:265713', 'chr10:266654',
             'chr10:267464', 'chr10:267551', 'chr10:267787', 'chr10:267911', 'chr10:267945', 'chr10:268109',
             'chr10:268330', 'chr10:268333', 'chr10:268441', 'chr10:268840', 'chr12:272213', 'chr12:274896',
             'chr12:275920', 'chr12:277543', 'chr12:277780', 'chr12:279740', 'chr14:273978', 'chr14:274882',
             'chr14:276050', 'chr14:276234', 'chr14:276638', 'chr14:277122', 'chr14:277397', 'chr11:270267',
             'chr11:270448', 'chr11:270516', 'chr11:271169', 'chr11:271246', 'chr11:271343', 'chr11:271388',
             'chr11:271905', 'chr11:273161', 'chr11:273197', 'chr11:273549', 'chr11:274648', 'chr11:274947',
             'chr11:275020', 'chr11:275064', 'chr11:278156', 'chr13:271118', 'chr13:271172', 'chr13:271191',
             'chr13:277409', 'chr13:278413', 'chr13:278451', 'chr10:271752', 'chr10:271970', 'chr10:272160',
             'chr10:275989', 'chr10:276100', 'chr10:276861', 'chr12:281662', 'chr12:282472', 'chr12:283035',
             'chr12:283680', 'chr12:284444', 'chr12:287062', 'chr12:287848', 'chr12:288249', 'chr12:288424',
             'chr14:280613', 'chr14:282149', 'chr14:284383', 'chr14:285094', 'chr14:285341', 'chr14:285928',
             'chr14:287833', 'chr14:288971', 'chr11:280859', 'chr11:282836', 'chr11:283458', 'chr11:285104',
             'chr11:285815', 'chr11:285816', 'chr11:287169', 'chr11:287742', 'chr11:288125', 'chr11:288400',
             'chr11:289506', 'chr13:280804', 'chr13:281454', 'chr13:281601', 'chr13:283299', 'chr13:285121',
             'chr13:286389', 'chr13:288135', 'chr13:288657', 'chr10:280076', 'chr10:280317', 'chr10:280563',
             'chr10:281752', 'chr10:282584', 'chr10:282631', 'chr10:282995', 'chr10:283438', 'chr10:283769',
             'chr10:284547', 'chr10:285446', 'chr10:286930', 'chr10:289442', 'chr12:291174', 'chr12:291302',
             'chr12:295285', 'chr12:296223', 'chr12:298998', 'chr12:299399', 'chr12:299412', 'chr12:299447',
             'chr12:299692', 'chr12:299725', 'chr14:290128', 'chr14:291059', 'chr14:291372', 'chr14:291417',
             'chr14:292243', 'chr14:293713', 'chr14:293838', 'chr14:294096', 'chr14:295396', 'chr14:296739',
             'chr14:298390', 'chr14:299063', 'chr14:299528', 'chr11:290482', 'chr11:293526', 'chr11:294083',
             'chr11:294697', 'chr11:295312', 'chr11:296991', 'chr11:297178', 'chr11:298641', 'chr11:299329',
             'chr10:290217', 'chr10:291028', 'chr10:291388', 'chr10:292655', 'chr10:292768', 'chr10:293752',
             'chr10:293913', 'chr10:295032', 'chr10:295097', 'chr10:298852', 'chr10:299255', 'chr10:299657',
             'chr13:290094', 'chr13:291380', 'chr13:291680', 'chr13:292490', 'chr13:293721', 'chr13:293941',
             'chr13:294016', 'chr13:295700', 'chr13:296470', 'chr13:296563', 'chr13:298028', 'chr13:298391',
             'chr13:298392', 'chr12:300530', 'chr12:302778', 'chr12:302894', 'chr12:303623', 'chr12:303644',
             'chr12:304010', 'chr12:304987', 'chr12:306643', 'chr12:307101', 'chr14:300057', 'chr14:300394',
             'chr14:300420', 'chr14:301821', 'chr14:301918', 'chr14:303431', 'chr14:304710', 'chr14:305413',
             'chr14:305855', 'chr14:307346', 'chr14:307693', 'chr14:307851', 'chr14:308322', 'chr14:308733',
             'chr14:309118', 'chr11:300028', 'chr11:300588', 'chr11:300841', 'chr11:302745', 'chr11:303428',
             'chr11:303637', 'chr11:305540', 'chr11:307142', 'chr11:308462', 'chr13:301602', 'chr13:302691',
             'chr13:308092', 'chr13:309608', 'chr13:309846', 'chr10:300365', 'chr10:300905', 'chr10:301199',
             'chr10:301389', 'chr10:302807', 'chr10:303465', 'chr10:303839', 'chr10:304412', 'chr10:304805',
             'chr10:306562', 'chr10:306710', 'chr10:306985', 'chr12:310420', 'chr12:310671', 'chr12:311266',
             'chr12:312128', 'chr12:312263', 'chr12:312874', 'chr12:313226', 'chr12:314161', 'chr12:317910',
             'chr12:318049', 'chr12:319631', 'chr11:310523', 'chr11:311155', 'chr11:311356', 'chr11:315452',
             'chr11:317072', 'chr11:317216', 'chr14:311586', 'chr14:312567', 'chr14:312646', 'chr14:317122',
             'chr14:318194', 'chr14:318961', 'chr14:319236', 'chr10:311004', 'chr10:311258', 'chr10:311454',
             'chr10:312391', 'chr10:312727', 'chr10:313075', 'chr10:313404', 'chr10:313420', 'chr10:313527',
             'chr10:315469', 'chr10:316780', 'chr10:318405', 'chr10:319320', 'chr13:310614', 'chr13:310758',
             'chr13:311261', 'chr13:311653', 'chr13:312585', 'chr13:313820', 'chr13:315942', 'chr13:318365',
             'chr13:318385', 'chr11:322647', 'chr11:323142', 'chr11:323230', 'chr11:324172', 'chr11:324740',
             'chr11:324802', 'chr11:324814', 'chr11:325194', 'chr11:326254', 'chr11:329245', 'chr12:321169',
             'chr12:321616', 'chr12:322275', 'chr12:322433', 'chr12:323862', 'chr12:324357', 'chr12:325217',
             'chr12:326748', 'chr12:326805', 'chr12:328899', 'chr10:322449', 'chr10:322921', 'chr10:325575',
             'chr10:326240', 'chr10:329429', 'chr13:320226', 'chr13:320771', 'chr13:321921', 'chr13:322698',
             'chr13:323692', 'chr13:324488', 'chr13:324906', 'chr13:325543', 'chr13:326682', 'chr13:327537',
             'chr13:327663', 'chr13:328695', 'chr14:321339', 'chr14:321367', 'chr14:321623', 'chr14:323266',
             'chr14:323367', 'chr14:324208', 'chr14:324450', 'chr14:326422', 'chr14:326716', 'chr14:327721',
             'chr14:328469', 'chr14:328537', 'chr14:329838', 'chr13:330339', 'chr13:331003', 'chr13:331228',
             'chr13:331830', 'chr13:332406', 'chr13:332671', 'chr13:332681', 'chr13:333470', 'chr11:332545',
             'chr11:332718', 'chr11:333125', 'chr11:333274', 'chr11:334310', 'chr11:334669', 'chr11:336907',
             'chr11:337499', 'chr11:338101', 'chr11:338904', 'chr11:339479', 'chr11:339586', 'chr11:339689',
             'chr11:339870', 'chr12:330490', 'chr12:331265', 'chr12:332168', 'chr12:333778', 'chr12:334877',
             'chr12:334987', 'chr12:335023', 'chr12:337363', 'chr12:338554', 'chr12:338767', 'chr12:338773',
             'chr10:330111', 'chr10:331022', 'chr10:331493', 'chr10:332490', 'chr10:333116', 'chr10:333495',
             'chr10:333525', 'chr10:333591', 'chr10:333973', 'chr10:334153', 'chr10:335030', 'chr10:335953',
             'chr10:336421', 'chr10:337171', 'chr10:338306', 'chr10:339960', 'chr14:330222', 'chr14:330975',
             'chr14:333112', 'chr14:334082', 'chr14:334576', 'chr14:336623', 'chr14:337177', 'chr14:337590',
             'chr14:339845', 'chr14:339863', 'chr15:1191', 'chr15:1713', 'chr15:1918', 'chr15:1939', 'chr15:2909',
             'chr15:2980', 'chr15:3082', 'chr15:4245', 'chr12:340209', 'chr12:342089', 'chr12:342679',
             'chr12:342794', 'chr12:343062', 'chr12:343071', 'chr12:346955', 'chr12:346972', 'chr12:346976',
             'chr12:349163', 'chr11:340516', 'chr11:340920', 'chr11:341176', 'chr11:342464', 'chr11:342507',
             'chr11:342970', 'chr11:343896', 'chr11:345099', 'chr11:345101', 'chr11:346578', 'chr11:348671',
             'chr11:349509', 'chr11:349859', 'chr14:340621', 'chr14:341183', 'chr14:341888', 'chr14:342778',
             'chr14:343383', 'chr14:344248', 'chr14:347328', 'chr14:349396', 'chr14:349742', 'chr10:341344',
             'chr10:342257', 'chr10:343025', 'chr10:343296', 'chr10:344191', 'chr10:345094', 'chr10:346088',
             'chr10:348410', 'chr10:349085', 'chr10:349130', 'chr10:349541', 'chr12:350410', 'chr12:350987',
             'chr12:352558', 'chr12:355941', 'chr12:356076', 'chr12:356278', 'chr12:357230', 'chr12:357305',
             'chr12:357682', 'chr12:358623', 'chr12:358843', 'chr11:350081', 'chr11:350539', 'chr11:351765',
             'chr11:351774', 'chr11:352874', 'chr11:354201', 'chr11:354821', 'chr11:355673', 'chr11:357187',
             'chr11:357476', 'chr11:357503', 'chr11:359043', 'chr10:351662', 'chr10:351793', 'chr10:354498',
             'chr10:355127', 'chr10:355133', 'chr10:356026', 'chr10:357616', 'chr10:357680', 'chr10:358598',
             'chr10:359472', 'chr10:359592', 'chr12:361946', 'chr12:362094', 'chr12:363320', 'chr12:363579',
             'chr12:363606', 'chr12:364193', 'chr12:364360', 'chr12:366887', 'chr12:368529', 'chr12:369028',
             'chr10:361572', 'chr10:361895', 'chr10:362481', 'chr10:362826', 'chr10:363057', 'chr10:364057',
             'chr10:364490', 'chr10:366123', 'chr10:367157', 'chr10:368443', 'chr10:368603', 'chr11:360407',
             'chr11:361058', 'chr11:363235', 'chr11:363744', 'chr11:363838', 'chr11:364217', 'chr11:365437',
             'chr11:366283', 'chr11:368024', 'chr12:370090', 'chr12:371107', 'chr12:373193', 'chr12:373687',
             'chr12:374667', 'chr12:374713', 'chr12:375324', 'chr12:377027', 'chr12:377484', 'chr12:377537',
             'chr12:377577', 'chr10:371030', 'chr10:371333', 'chr10:371411', 'chr10:372214', 'chr10:372815',
             'chr10:372834', 'chr10:373722', 'chr10:374819', 'chr10:375372', 'chr10:376305', 'chr10:378954',
             'chr11:370606', 'chr11:374905', 'chr11:375628', 'chr11:375964', 'chr11:376283', 'chr11:376711',
             'chr11:377280', 'chr11:378556', 'chr11:379962', 'chr12:381922', 'chr12:382949', 'chr12:383711',
             'chr12:384589', 'chr12:385876', 'chr12:386648', 'chr12:388477', 'chr12:389531', 'chr11:379980',
             'chr11:381644', 'chr11:384717', 'chr11:385671', 'chr11:386554', 'chr11:387958', 'chr11:388341',
             'chr11:388810', 'chr11:389466', 'chr10:381125', 'chr10:381863', 'chr10:382055', 'chr10:383076',
             'chr10:383448', 'chr10:383860', 'chr10:384350', 'chr10:384528', 'chr10:384837', 'chr10:386638',
             'chr10:386812', 'chr10:389731', 'chr12:393456', 'chr12:393747', 'chr12:394409', 'chr12:396118',
             'chr12:396392', 'chr12:397746', 'chr12:398346', 'chr11:390241', 'chr11:391086', 'chr11:391938',
             'chr11:392240', 'chr11:392607', 'chr11:392825', 'chr11:395150', 'chr11:395225', 'chr11:395449',
             'chr11:397797', 'chr11:398848', 'chr11:398874', 'chr11:399634', 'chr10:391607', 'chr10:392068',
             'chr10:393122', 'chr10:394305', 'chr10:394331', 'chr10:394450', 'chr10:394924', 'chr10:395162',
             'chr10:395557', 'chr10:395901', 'chr10:396130', 'chr10:398557', 'chr10:398840', 'chr10:399590',
             'chr10:399902', 'chr12:402469', 'chr12:402548', 'chr12:402842', 'chr12:402960', 'chr12:403701',
             'chr12:403962', 'chr12:404414', 'chr12:404636', 'chr12:405161', 'chr12:406868', 'chr12:406889',
             'chr12:407089', 'chr12:407981', 'chr12:409022', 'chr12:409283', 'chr11:402275', 'chr11:402329',
             'chr11:403711', 'chr11:404397', 'chr11:405363', 'chr11:405382', 'chr11:405796', 'chr11:406857',
             'chr11:406903', 'chr11:408045', 'chr11:408501', 'chr11:408741', 'chr11:408947', 'chr11:409476',
             'chr11:409891', 'chr11:409949', 'chr10:400375', 'chr10:402081', 'chr10:402532', 'chr10:404436',
             'chr10:404438', 'chr10:405853', 'chr10:406445', 'chr10:408514', 'chr10:409407', 'chr10:409509',
             'chr12:411113', 'chr12:411442', 'chr12:412491', 'chr12:412931', 'chr12:412937', 'chr12:413097',
             'chr12:414725', 'chr12:414976', 'chr12:416995', 'chr12:419595', 'chr11:410002', 'chr11:410409',
             'chr11:411549', 'chr11:412362', 'chr11:415013', 'chr11:416282', 'chr11:417864', 'chr10:410996',
             'chr10:411731', 'chr10:412286', 'chr10:413635', 'chr10:413685', 'chr10:414152', 'chr10:414315',
             'chr10:415433', 'chr10:415501', 'chr10:415563', 'chr10:417121', 'chr10:418622', 'chr10:419053',
             'chr10:421341']

# missing and low count sites should be excluded in matrix
missing_and_low_count = AggregateMatrix(file_list=test_cgmap_file[0:3], min_site_coverage=10,
                                        site_proportion_threshold=.9, verbose=True)
missing_and_low_count.aggregate_matrix()

# missing sites with low count should be included in matrix
missing_and_five_count = AggregateMatrix(file_list=test_cgmap_file[0:3], min_site_coverage=5,
                                         site_proportion_threshold=.9, verbose=True)
missing_and_five_count.aggregate_matrix()

# cg only sites
cg_only_test = AggregateMatrix(file_list=test_cgmap_file, min_site_coverage=5,
                               site_proportion_threshold=.9, verbose=True, cg_only=True)
cg_only_test.aggregate_matrix()


# cg only high proportion
cg_only_test_high = AggregateMatrix(file_list=test_cgmap_file, min_site_coverage=10,
                                    site_proportion_threshold=1, verbose=True, cg_only=True)
cg_only_test_high.aggregate_matrix()


# test_command line
test_matrix_output = f'{test_directory}/TestData/test_cgmap_files/matrix_test.txt'

bsb_matrix_commands = ['python3', bsbolt, 'AggregateMatrix',
                       '-F', f'{test_cgmap_file[0]},{test_cgmap_file[1]},{test_cgmap_file[2]}',
                       '-S', f'S1,S2,S3', '-O', test_matrix_output,
                       '-verbose', '-min-coverage', '10', '-min-sample', '0.9']
subprocess.run(bsb_matrix_commands)

test_matrix, test_site_order, test_samples = get_bsb_matrix(test_matrix_output)


class TestMatrixAggregation(unittest.TestCase):

    def setUp(self):
        pass

    def test_site_missing_low_count(self):
        # test site missing in 2.cgmap and low coverage in 3.cgmap are not included
        for site in val_sites:
            self.assertNotIn(site, missing_and_low_count.collapsed_matrix)

    def test_five_count(self):
        # test sites missing in 2.cgmap and low coverage in 3.cgmap are included with lower read count threshold
        for site in val_sites:
            self.assertIn(site, missing_and_five_count.collapsed_matrix)

    def test_cg_only(self):
        # test only cg sites are included
        self.assertEqual(len(cg_only_test.collapsed_matrix), 22344)

    def test_cg_only_high(self):
        # test missing and low count cg sites are not included in final matrix
        self.assertEqual(len(cg_only_test_high.collapsed_matrix), 19120)

    def test_command_line(self):
        for site in val_sites:
            self.assertNotIn(site, test_site_order)


if __name__ == '__main__':
    unittest.main()
