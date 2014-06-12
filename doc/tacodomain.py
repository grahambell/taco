from sphinxcontrib.domaintools import custom_domain

def setup(app):
    app.add_domain(custom_domain('TacoDomain',
        name='taco',
        label='Taco',
        elements={
            'action': {
                'objname': 'Action',
                'indextemplate': 'single: %s',
            },
            'object': {
                'objname': 'Special Object',
                'indextemplate': 'single: %s',
            },
        }))
