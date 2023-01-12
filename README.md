# ssh-tunnel-wizard

A small python utility for forwarding ports to remote machine.

## Why

I created this utility code a while ago to be able to forward ports from a machine hidden behind a NAT layer to a publicly accessible VPS. Most of the changes where not tracked on the GitHub since it was only for one device and wasn't too complex. However, recently I needed another device to forward its ports too, and realized how versatile it is, by simply modifying the `tunnel_config.yaml` file.

## Usage/How-To

In order to use and customize this utility, only the `tunnel_config.yaml` file needs to be modified. The config file consists of the following options:

* `hostname`: The hostname or the IP address that SSH will use to connect to the remote device.
  * You can use custom hostnames with SSH by modifying the `/etc/ssh/ssh_config` file. This way you can also add proxies or modify connection paramenters.
* `port`: The port on the remote machine that can be used to connect back to the local machine.
  * This is was previously to check if the tunnel is alive, but I kept it as it comes in really handy in connecting to the NAT-hidden machine from anywhere in the world.
* `username`: The remote username to connect to while creating an SSH tunnel.
  * Make sure the public SSH key of the username you will use is registered with that user, using `ssh-copy-id` command.
  * If you do not use pubkey authentication, the SSH will likely ask you for a password of the remote user.
* `tunneled_ports`: The list of ports to tunnel using the SSH port tunneling convention. This option allows you to specify the:
  * `dest_ip`: *(default: localhost)* The destination IP address that can access the tunneled port. Use the `GatewayPorts clientspecified` option in the remote machine `/etc/ssh/sshd_config` file. It is usually set to either:
    * `localhost` to make it only accessible on the remote machine, or
    * `0.0.0.0` to make the port publicly accessible.
  * `dest_port`: The destination port which is accessible on the remote machine.
  * `local_ip`: The local IP address whose port will be tunneled. Often `localhost`, but can also be any accessible device, including any device on the local LAN.
  * `local_port`: The port of the local device that is to be tunneled. (Seems self-explanatory.)
