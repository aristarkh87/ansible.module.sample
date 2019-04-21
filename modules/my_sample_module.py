#!/usr/bin/python

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: my_sample_module

short_description: This is my sample module

version_added: "2.4"

description:
    - "This is my longer description explaining my sample module"

options:
    name:
        description:
            - Your name
        required: true
    email:
        description:
            - Your email
        required: true
    status:
        description:
            - "Status: single or married"
        required: false
        default: single

author:
    - Oleg Dolgikh (aristarkh@aristarkh.net)
'''

EXAMPLES = '''
'''

RETURN = '''
result:
    description: The dict with params
    type: dict
'''

from ansible.module_utils.basic import AnsibleModule


def run_module(module):
    if '@' not in module.params['email']:
        module.fail_json(msg='Wrong email')
    return module.params


def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', required=True),
            email=dict(type='str', required=True),
            status=dict(type='str', required=False, default="single")
        ),
        supports_check_mode=False
    )

    result = dict(
        changed=False
    )

    result['result'] = run_module(module)

    module.exit_json(**result)


if __name__ == '__main__':
    main()
