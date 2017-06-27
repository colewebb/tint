# Tint

File sharing over a local network

# Tint Protocol Overview

## Initial connection

Client sends line of form:

`tint version-number system-type ip-address mac-address`

Host responds with the same information. Any deviation terminates the connection and marks the host as not a tint host.

## File Transfer

Client sends line of form:

`tint version-number send filename filesize`

Host responds with line of form, while waiting for user to accept or decline reciept of the file:

`tint version-number acknowledge filename filesize`

If the user accepts the file, host responds with:

`tint version-number accept filename filesize`

If the user declines the file, host responds with:

`tint version-number decline filename filesize`
