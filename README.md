## Python Bottle Framework Skeleton for Google App Engine

A skeleton for building Python applications on Google App Engine with the
[Bottle micro framework](http://bottlepy.org) version 0.11.6

## Run Locally
1. Install the [Google Cloud SDK](https://developers.google.com/cloud/sdk/).
   (Note that You'll also need python 2.7 and [pip 1.4 or later](http://www.pip-installer.org/en/latest/installing.html) installed).

2. Clone this repository:

   ```
   git clone https://github.com/GoogleCloudPlatform/appengine-python-bottle-skeleton.git
   ```
3. Install third-party dependencies in the project's `lib/` directory:
   (App Engine requires that project dependencies be installed inside
   the project directory in order to be deployed with your
   application).
   ```
   cd appengine-python-bottle-skeleton
   pip install -r requirements.txt -t lib/
   ```
4. Run this project with the Local Developer Server:

   ```
   dev_appserver.py appengine-python-bottle-skeleton
   ```
5. Open [http://localhost:8080](http://localhost:8080) in your browser .

See [the development server documentation](https://developers.google.com/appengine/docs/python/tools/devserver)
for options when running dev_appserver.

## Deploy
To deploy the application:

1. Use the [Google Developers Console](https://cloud.google.com/console?getstarted=https://cloud.google.com/products/app-engine) to create an app and
   get your project id.
1. [Deploy the
   application](https://developers.google.com/appengine/docs/python/tools/uploadinganapp) with

```
appcfg.py -A <your-project-id> --oauth2 update .
```
1. Congratulations! Your application is now live at your-project-id.appspot.com


### Feedback
Star this repo if you found it useful. Use the github issue tracker to give
feedback on this repo and to ask for skeletons for other frameworks.

## Contributing changes
See [CONTRIB.md](CONTRIB.md)

## Licensing
See [LICENSE](LICENSE)

## Authors
Logan Henriquez
Johan Euphrosine