# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="tmux_cssh",
    version="1.0",
    packages=find_packages(),
    description=(
        'Simple script to provide cssh/ClusterSSH like functionality using'
        ' only tmux'),
    install_requires=[
        'sarge',
        'tmuxp',
    ],
    entry_points={
        'console_scripts': [
            'tmux_cssh = tmux_cssh.cli:tmux_cssh',
            'tmux_cluster = tmux_cssh.cli:tmux_cluster',
        ]
    },
)
