# Goblin Game :boom::boom:

## Table of Contents
1. [Game description](#game-description)
2. [Display pictures](#display-pictures)
3. [About the Code](#about-the-code) 
    - [Music and Sound effects](#music-and-sound-effects)
    - [Walking effect of player](#walking-effect-of-the-player)
    - [Making the player jump](#making-the-player-jump)
4. [How to play](#how-to-play)
5. [References](#references)

<br><br><br><br>
### <center>Game Description</center><br><br>
This is a single player game.The goal of the game is simple - survive.In order to survive you must kill the enemy goblins before they try to kill you.By killing the goblins you get more score.<br><br>To kill the goblin you can use your plasma gun or your plasma bomb.The plasma bomb can kill all the goblins present, but it takes time to reload the bome so use it wisely.After some time you will also get a health box to increase your health.More information on How to play the game can be found in the 'How to Play' section in the game's main menu<br><br><br><br>

### <center>Display Pictures</center><br><br>
![Main menu](readme_pics/ss1.PNG)
![GamePlay](readme_pics/ss2.PNG)<br>

### <center>About the Code</center><br><br>

#### Music and Sound effects
This game uses a lot of sound effects.There is a music in the background and sounds for bullet shooting,bullet hitting,jumping and bomb explosion.
<br>
First of all you should have a music file (format - mp3,wav,ogg).For the background music you should have a longer file and for the sound effects you should have a shorter music file.
After you have your music files, you need to load them as Sound objects in the program.Background music and sound effects are loaded and played differently.<br>For the background music - <br>
```background_music = pygame.mixer.music.load(os.path.join(os.path.dirname(__file__),background_music_file_name.extension))```<br>
here ```background_music``` is the Sound object which can be used to play the sound.<br>
and ```background_music_file_name.extension``` is the name of our music file with extension(example - music.mp3)<br>
For the Sound effects - <br>
```sound_effect = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__),"filename.wav"))```<br>
here ```sound_effect``` is the Sound object which can be used to play the sound.<br><br>
Now we have just loaded the sounds. Now lets see how to play them.<br>
To play the background music we can use - <br>
```pygame.mixer.music.play(loops=0, start=0.0, fade_ms = 0)```<br>
here,<br>
loops - number of times the music should repeat. It's default value is 0.To play the music on an infinite loop set loops=-1.<br>
start - denotes the position in time, the music starts playing from. Which is 0.0 by default.<br>
fade_ms - makes the music start playing at 0 volume and fade up to full volume over the given time.<br>
All these are optional arguments.
<br><br><br>
#### Walking effect of the player
When the player is moving the player appears to be walking. This can be done using 10-15 images of the character, each of which is slightly different than the previous image.These images which are used in this project can be found [here](pics). Then all we need to do is whenever the player is moved we display the slightly different image at a position  little ahead of the previous position. In order to keep track of all these images we can make use a List image_list and then just display the image_list[i].Now if we have to change the image all we need do is change the index i to (i+1)%(number_of_images).   
<br><br><br>
#### Making the player jump
When the up arrow key is pressed the player can jump.To give this effect we have see 2 things.<br>
First is that game contains a game loop which runs infinitely.To keep the framerate less than a specific value we can use - <br>
```pygame.time.Clock().tick(desired_frame_rate)``` - Now the program will never run faster than the desired framerates.<br>
So now we can assume that the program runs for the desired framerates(fr) per second.This means that interval between any two frames is 1/(fr).This will be our unit time.<br><br>
Now to make the player jump we will use concepts of physics.<br>
- When the player has to jump.Then he/she should have an upward velocity.
- After each unit time the vertical displacement of the player has to change by this vertical velocity.
- After each unit time this vertical velocity has to change by some vertical acceleration.
Now to simulate this we make three variables,<br>
- player vertical displacement(height above the ground while jumping)  -   p_dis
- player vertical velocity     -   p_vel
- player vertical acceleration(gravity)    -   p_acc
Now initially we have to set ```p_dis = 0``` and ```p_acc = x``` where x is positive number which gives the best jumping effect.(acceleration is downwards and in pygame Y coordinate increases in teh downward direction, so acceleration should be positive).<br>
When we press the up arrow key, we set the ```p_vel = y``` where y is negative number which gives the best jumping effect.(velocity is upward and in pygame Y coordinate decreases in the upward direction, so velocity should be negative).<br>
Now all we have to do this in every frame change these values accordingly.<br>
```p_dis = p_dis+p_vel```<br>
```p_vel = p_vel+p_acc```
<br><br><br><br>
### <center>How to play</center><br><br>
<p align="center">
    <img src="https://github.com/IshanMehta115/Goblin-Game/blob/main/pics/how_to_play_1.jpg" alt="how to play 1" width="300px">
    <img src="https://github.com/IshanMehta115/Goblin-Game/blob/main/pics/how_to_play_2.jpg" alt="how to play 2" width="300px">
    <img src="https://github.com/IshanMehta115/Goblin-Game/blob/main/pics/how_to_play_3.jpg" alt="how to play 3" width="300px">
    <img src="https://github.com/IshanMehta115/Goblin-Game/blob/main/pics/how_to_play_4.jpg" alt="how to play 4" width="300px">
    <img src="https://github.com/IshanMehta115/Goblin-Game/blob/main/pics/how_to_play_5.jpg" alt="how to play 5" width="300px">
    <img src="https://github.com/IshanMehta115/Goblin-Game/blob/main/pics/how_to_play_6.jpg" alt="how to play 6" width="300px">
    <img src="https://github.com/IshanMehta115/Goblin-Game/blob/main/pics/how_to_play_7.jpg" alt="how to play 7" width="300px">
    <img src="https://github.com/IshanMehta115/Goblin-Game/blob/main/pics/how_to_play_8.jpg" alt="how to play 8" width="300px">
</p>
 
### <center>References</center><br><br>
Here are some references for learning more about this project.<br>
For pygame functions and examples
- [pygame documentaion](https://www.pygame.org/docs/)
