**UFW Tactical Command Table (Electronics) Manual**
=====================================================

Table of Contents
-----------------

1. [Introduction](#introduction)
2. [Command Structure](#command-structure)
3. [Commands and Options](#commands-and-options)
4. [Examples](#examples)

### Introduction

The UFW Tactical Command Table (ELECTRONICS) is a comprehensive guide to configuring and managing your electronic devices using the Uncomplicated Firewall (UFW). This manual will walk you through the available commands, options, and examples to help you effectively use UFW for your electronic needs.

### Command Structure

The command structure for UFW is as follows:

`ufw <command> [options]`

Where `<command>` is one of the following:

* `allow`
* `deny`
* `delete`
* `insert`
* `reload`
* `status`
* `loglevel`
* `logging`

### Commands and Options

#### allow

Allow incoming or outgoing traffic on a specific port or protocol.

`ufw allow [direction] <port>[/protocol]`

* `[direction]`: Specify the direction of traffic (inbound, outbound, or both).
* `<port>`: The port number to allow.
* `[/protocol]`: Optional protocol specification (tcp, udp, icmp, etc.).

Example:
```bash
ufw allow in 22/tcp
```
Allows incoming TCP traffic on port 22.

#### deny

Deny incoming or outgoing traffic on a specific port or protocol.

`ufw deny [direction] <port>[/protocol]`

* `[direction]`: Specify the direction of traffic (inbound, outbound, or both).
* `<port>`: The port number to deny.
* `[/protocol]`: Optional protocol specification (tcp, udp, icmp, etc.).

Example:
```bash
ufw deny out 80/tcp
```
Denies outgoing TCP traffic on port 80.

#### delete

Delete a rule from the UFW configuration.

`ufw delete <rule>`

* `<rule>`: The number or description of the rule to delete.

Example:
```bash
ufw delete 1
```
Deletes the first rule in the UFW configuration.

#### insert

Insert a new rule at a specific position in the UFW configuration.

`ufw insert [position] <rule>`

* `[position]`: Specify the position where the rule should be inserted (before, after, or at).
* `<rule>`: The number or description of the rule to insert.

Example:
```bash
ufw insert 1 allow in 22/tcp
```
Inserts a new rule allowing incoming TCP traffic on port 22 as the first rule.

#### reload

Reload the UFW configuration from disk.

`ufw reload`

Example:
```bash
ufw reload
```
Reloads the UFW configuration from disk.

#### status

Display the current UFW configuration.

`ufw status [verbose]`

* `[verbose]`: Optional flag to display detailed information about each rule.

Example:
```bash
ufw status verbose
```
Displays a detailed list of all rules in the UFW configuration.

#### loglevel

Set the logging level for UFW.

`ufw loglevel <level>`

* `<level>`: The desired logging level (low, medium, high, or debug).

Example:
```bash
ufw loglevel medium
```
Sets the logging level to medium.

#### logging

Enable or disable logging for UFW.

`ufw logging [on|off]`

* `[on|off]`: Optional flag to enable or disable logging.

Example:
```bash
ufw logging on
```
Enables logging for UFW.

### Examples

Here are some examples of using the UFW Tactical Command Table (ELECTRONICS):

1. Allow incoming SSH traffic on port 22:

`ufw allow in 22/tcp`

2. Deny outgoing HTTP traffic on port 80:

`ufw deny out 80/tcp`

3. Delete the first rule from the UFW configuration:

`ufw delete 1`

4. Insert a new rule allowing incoming FTP traffic on port 21 as the second rule:

`ufw insert 2 allow in 21/tcp`

5. Reload the UFW configuration from disk:

`ufw reload`

6. Display the current UFW configuration with detailed information about each rule:

`ufw status verbose`

7. Set the logging level to medium:

`ufw loglevel medium`

8. Enable logging for UFW:

`ufw logging on`

By following this manual, you should be able to effectively use the UFW Tactical Command Table (ELECTRONICS) to configure and manage your electronic devices using the Uncomplicated Firewall (UFW).