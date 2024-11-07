  * [Getting Started](../../guide/programming/index.html)
  * [Guides](../../guide/index.html)
  * [API Reference](../../api/index.html)
  * [Tutorials](../../tutorial/index.html)
  * [Plugins](../../plugin/index.html)
  * [Solar2D Native](../../native/index.html)
  * [CoronaCards](../../coronacards/index.html)

  * supersonic.init()
    * Overview
    * Syntax
      * adListener (required)
      * params (required)
    * Parameter Reference
      * appKey (required)
      * hasUserConsent (optional)
    * Example

[Documentation](https://docs.coronalabs.com) ▸
[Plugins](../../plugin/index.html) ▸
[Supersonic](../../plugin/supersonic/index.html) ▸
[init](../../plugin/supersonic/init.html)

# supersonic.init()

> **Type** | [Function](../../api/type/Function.html)  
> ---|---  
> **Return value** | none  
> **Revision** | [Release 2024.3703](https://solar2d.com/download/)  
> **Keywords** | ads, advertising, Supersonic, init  
> **See also** | [supersonic.load()](../../plugin/supersonic/load.html)  
> | [supersonic.show()](../../plugin/supersonic/show.html)  
> | [supersonic.*](../../plugin/supersonic/index.html)  
  
## Overview

`supersonic.init()` initializes the Supersonic plugin.

Once initialized, you can load an ad using
[supersonic.load()](../../plugin/supersonic/load.html) and subsequently show
it via [supersonic.show()](../../plugin/supersonic/show.html).

## Syntax

    
    
    supersonic.init( adListener, params )

##### adListener (required)

_[Listener](../../api/type/Listener.html)._ Listener function that will
receive [adsRequest](../../plugin/supersonic/event/adsRequest/index.html)
events.

##### params (required)

_[Table](../../api/type/Table.html)._ Table containing Supersonic
initialization values — see the next section for details.

## Parameter Reference

The `params` table includes initialization properties for the Supersonic
plugin.

##### appKey (required)

_[String](../../api/type/String.html)._ Your Supersonic app key, retrieved
from the [Supersonic developer
portal](https://platform.supersonic.com/partners/).

##### hasUserConsent (optional)

_[Boolean](../../api/type/Boolean.html)._ If set to `false`, Chartboost will
enable GDPR data collection restrictions, set to `true` for opposite. Default
is `false`.

## Example

    
    
    local supersonic = require( "plugin.supersonic" )
    
    local function adListener( event )
    
        if ( event.phase == "init" ) then  -- Successful initialization
            print( event.isError )
        end
    end
    
    -- Initialize the Supersonic plugin
    supersonic.init( adListener, { appKey="YOUR_APP_KEY" } )

* * *

© 2020-2024 Solar2D All Rights Reserved.

Help us help you! If you notice a problem with this page, please report it.

[Report an Issue](https://github.com/coronalabs/corona-docs/issues)

