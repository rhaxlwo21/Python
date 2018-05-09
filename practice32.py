#heroes 리스트에서 hero가 존재하는 여부 확인
heroes = ['아이언맨','토르','헐크','스칼렛 위치']

hero = input("영웅의 이름을 입력하세요:")

if hero in heroes:
    print(hero,'은(는) 어벤져스 입니다.')
    print(heroes.index(hero),"번 인텍스에 있습니다.")
else:
    print(hero,"은(는) 어벤져스가 아닙니다")
