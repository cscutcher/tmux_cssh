tmux_cssh
=========

Simple script to provide cssh/ClusterSSH like functionality using only tmux

Install
-------

Requires tmux.. obviously.

Install with;

```bash
pip install tmux_cssh
```

Usage
-----

For connecting to multiple ssh servers;

```bash
tmux_cssh host1.domain.com host2.domain.com host3.domain.com
```

If you want to customise how you're calling ssh instead use;

```bash
tmux_cluster 'ssh host1.domain.com' 'ssh host2.domain.com' 'ssh host3.domain.com'
```
