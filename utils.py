import requests
import os


def get_input(day):
    response = 
requests.get(f'https://adventofcode.com/2023/day/{day}/input',
                            cookies={'session': 
os.getenv('AOC_SESSION_TOKEN')})
    assert response.ok
    return response.text.strip()


def get_input_lines(day):
    return get_input(day).split('\n')
