# install cowsay
cowsay:
  pkg.installed

# write motd
write_motd:
  cmd.run:
    - name: "cowsay {{ pillar['motd']['cow_type'] }} {{ pillar['motd']['text'] }} > /etc/motd"
