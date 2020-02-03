from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client.pymongo_test

camera_settings = db.camera_settings

## Creating
camera_mode_0 = {
    'Resolution': '2448x2048',
    'Exposure': 5000,
    'FlashOn': True
}
result = camera_settings.insert_one(camera_mode_0)

## Reading
print('cam data: {0}'.format(result.inserted_id))

## Updating
camera_mode_1 = {
    'Resolution': '2448x2048',
    'Exposure'  : 5000,
    'FlashOn'   : False
}
camera_mode_2 = {
    'Resolution': '1224x1024',
    'Exposure'  : 2000,
    'FlashOn'   : True
}
camera_mode_3 = {
    'Resolution': '2448x2048',
    'Exposure'  : 5000,
    'FlashOn'   : False
}
new_result = camera_settings.insert_many([camera_mode_1, camera_mode_2, camera_mode_3])
print('Multiple cam data: {0}'.format(new_result.inserted_ids))

## Reading, I guess
max_res = camera_settings.find_one({'Resolution': '2448x2048'})
print(max_res)

all_max_res = camera_settings.find({'Resolution': '2448x2048'})
print(all_max_res)
for one_mode in all_max_res:
    print(one_mode)

