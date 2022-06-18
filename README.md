# disc-back

it is powered in https://disc-back.vercel.app/ 

* each change in git repo will trigger auto build, see vercel https://vercel.com/larrycai/disc-back/deployments
* if it is failure, check functions (log) 
* module is defined in [requirements.txt](requirements.txt)
* enabled WSGI at root in [vercel.json](vercel.json)

redis database is powered on https://upstash.com/

# reference

* https://vercel.com/docs/runtimes#advanced-usage/advanced-python-usage
* https://dev.to/andrewbaisden/how-to-deploy-a-python-flask-app-to-vercel-2o5k
