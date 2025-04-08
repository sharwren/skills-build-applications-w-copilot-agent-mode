DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'octofit_db',
        'HOST': 'localhost',
        'PORT': 27017,
    },
    'spare': {
        'ENGINE': 'djongo',
        'NAME': 'spare_db',
        'HOST': 'localhost',
        'PORT': 37017,
    }
}