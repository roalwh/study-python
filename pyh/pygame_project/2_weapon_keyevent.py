import pygame
import os

# 초기화(반드시 필요)
pygame.init()  

# 화면 크기 설정
screen_width = 640  # 가로크기
screen_height = 480  # 세로크기
screen = pygame. display.set_mode((screen_width, screen_height))
# 화면 타이틀 설정
pygame. display.set_caption("game")

# FPS
clock = pygame.time.Clock()

##########################################################################################
#1. 사용자 게임 초기화(배경화면,게임이미지,좌표,속도,폰트 등)
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path,"images")

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스태이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] #높이위에 캐릭터를 두기위 해 사용

#캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height

#캐릭터 이동 방향
character_to_x = 0

#캐릭터 이동 속도
character_speed= 0.6

#무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

#무기는 한번에 여러발 발사 가능
weapons = []

#무기이동속도
weapon_speed = 10



running = True  # 게임이 진행중인가?
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수를 설정

    #2. 이벤트 처리 (키보드,마우스 등)
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False
  
    # 방향키 상하좌우 이동 설정
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            character_to_x -= character_speed
        elif event.key == pygame.K_RIGHT:
            character_to_x += character_speed
        elif event.key == pygame.K_SPACE:
            weapon_x_pos = character_x_pos + (character_width /2 ) - (weapon_width/2)
            weapon_y_pos = character_y_pos
            weapon.append([weapon_x_pos,weapon_y_pos])

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            character_to_x=0

    
    #3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x

    if character_x_pos <0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    #4. 충돌처리
    
    #5. 화면에 그리기
    screen.blit(background,(0,0)) #오른쪽 상단 기준
    screen.blit(stage,(0,screen_height - stage_height)) 
    screen.blit(stage,(0,screen_height - stage_height)) 
    screen.blit(character, (character_x_pos, character_y_pos))

    for weapon_x_pos,weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos,weapon_y_pos))

    pygame.display.update()

# pygame 종료
pygame.quit()
