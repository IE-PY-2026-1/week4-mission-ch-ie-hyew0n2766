# 파일이름 : 도장 깨기! 나만의 맛집 버킷리스트
# 작 성 자 : Kim hyewon

bucket_list =[]
list_1 = input('맛집 리스트 입력: ')
list_2 = input('맛집 리스트 입력: ')
list_3 = input('맛집 리스트 입력: ')
bucket_list.append(list_1)
bucket_list.append(list_2)
bucket_list.append(list_3)
print({f'리스트: {bucket_list}'})
vip = input('1순위 VIP 맛집: ')
bucket_list.insert(0,f"{vip}")
print({f'리스트: {bucket_list}'})
visited = input('도장 깨기: ')
bucket_list.remove(visited)
print({f'리스트: {bucket_list}'})
