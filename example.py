"""Run an example script to quickly test any SimpliSafe system."""
# pylint: disable=protected-access

import asyncio

from aiohttp import ClientSession

from pikrellcam_python import PiKrellCam
from aiohttp.client_exceptions import ClientError, ClientResponseError


async def exercise_client(
        host: str, port: str, user: str, password: str, websession: ClientSession) -> None:
    """Test a SimpliSafe client (regardless of version)."""
    print('User:{0} @ {1}'.format(user, host))
    print('========================')
    try:
        camera = await PiKrellCam.login(host,port,user, password, websession)
        await camera.update()
        value =  await camera.is_motion_enabled()
        print('Motion Enable is:{0}'.format(value))
        value =  await camera.is_recording()
        print('Recording State is:%s' % value)
    except (ClientError, ClientResponseError) as ex:
        print('Unable to connect to PiKrellCam:{0}'.format(str(ex)))


async def main() -> None:
    """Create the aiohttp session and run the example."""
    async with ClientSession() as websession:
        print()
        await exercise_client('10.0.1.4', '8080', 'pi', 'darius', websession)
 

asyncio.get_event_loop().run_until_complete(main())
