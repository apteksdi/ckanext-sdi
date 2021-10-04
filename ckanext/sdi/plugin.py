import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class SDIPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IFacets, inherit=True)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'sdi')

    # IFacets
    def dataset_facets(self, facets_dict, package_type):
        return OrderedDict([
            ('organization', _(u'Organization')),
            ('groups', _(u'Group')),
            # ('tags', _(u'Keyword')),

            # ('res_format', _(u'Format')),
            # ('accrualPeriodicity', _(u'Update frequency')),
            # ('datatype', _(u'Type')),
            # ('tags', _(u'Mot-clé')),
        ])