#!/usr/bin/env python

from random import choice
import os
from time import sleep

from IPython import embed
import click
import vlc

HERE = os.path.abspath(os.path.dirname(__file__))
sound_dir = os.path.join(HERE, 'sound')

@click.group()
def cli():
    pass

@click.command()
@click.argument('pinyin_1')
@click.argument('pinyin_2')
def compare(pinyin_1, pinyin_2):
    click.echo('Compare %s with %s'%(pinyin_1, pinyin_2))

    i = 1
    while True:
        for pinyin in [pinyin_1, pinyin_2]:
            pinyin_path = os.path.join(sound_dir, "%s.mp3"%pinyin)
            if os.path.exists(pinyin_path):
                player = vlc.MediaPlayer(pinyin_path)
                player.play()
                sleep(4)
                player.release()
                click.echo(i)
            else:
                raise Exception("Pinyin file (%s) not found!"%pinyin_path)
            i += 1


@click.command()
def play():
    click.echo('Playing...')

    pinyin_list = os.listdir(sound_dir)

    while True:
        pinyin_file = choice(pinyin_list)
        answer = pinyin_file.split('.')[0]

        pinyin_path = os.path.join(sound_dir, pinyin_file)
        player = vlc.MediaPlayer(pinyin_path)
        player.play()

        input_ = raw_input("Answer:")
        if input_ != 'q':
            if input_ == answer:
                click.echo('Correct!')
            else:
                click.echo('***Incorrect!***')
                click.echo('The correct answer is: %s'%answer)
        else:
            break

        player.release()

cli.add_command(play)
cli.add_command(compare)
