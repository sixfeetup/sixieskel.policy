import copy
from templer.core.base import get_var
from templer.core.vars import EASY
from templer.core.vars import EXPERT
from templer.core.vars import StringVar
from templer.plone.plone import Plone
from sixieskel.policy.utils import run_cmd


class SixiePolicy(Plone):

    summary = "A policy package following the Six Feet Up standards"
    help = "A package that will manage a Plone installation"
    category = "Six Feet Up"
    required_templates = ['plone_basic']
    _template_dir = "templates/policy"
    vars = copy.deepcopy(Plone.vars)
    vars.append(
        StringVar(
            'staff_password',
            'Enter the Staff password (leave blank for auto generated)',
            modes=(EXPERT,),
            )
        )
    vars.append(
        StringVar(
            'plone_version',
            'Plone version',
            default='4.1',
            modes=(EASY, EXPERT),
           )
    )
    get_var(vars, 'add_profile').default = True
    get_var(vars, 'version').default = '1.0'
    get_var(vars, 'author').default = 'Six Feet Up, Inc.'
    get_var(vars, 'author_email').default = 'info@sixfeetup.com'
    get_var(vars, 'url').default = 'http://www.sixfeetup.com'
    get_var(vars, 'keywords').default = 'zope plone policy'

    def check_vars(self, vars, cmd):
        responses = super(SixiePolicy, self).check_vars(vars, cmd)
        if not vars['staff_password']:
            # for this to work you'll need pwgen installed
            passwd = run_cmd('pwgen -acn 9 1')
            if not passwd:
                passwd = 'fjosu7aw'
            responses['staff_password'] = passwd
        return responses
