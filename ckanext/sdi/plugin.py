from collections import OrderedDict
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
    # def dataset_facets(self, facets_dict, package_type):
    #     return OrderedDict([
    #         ('organization', (u'Organization')),
    #         ('groups', (u'Group')),
    #         ('tags', (u'Keyword')),

    #         ('res_format', (u'Format')),
    #         # ('accrualPeriodicity', _(u'Update frequency')),
    #         # ('datatype', _(u'Type')),
    #         # ('tags', _(u'Mot-clé')),
    #     ])
    
    # def organization_facets(self, facets_dict, package_type):
    #     return OrderedDict([
    #         # ('organization', (u'Organization')),
    #         ('groups', (u'Group')),
    #         ('tags', (u'Keyword')),

    #         ('res_format', (u'Format')),
    #         # ('accrualPeriodicity', _(u'Update frequency')),
    #         # ('datatype', _(u'Type')),
    #         # ('tags', _(u'Mot-clé')),
    #     ])

    # def group_facets(self, facets_dict, package_type):
    #     return OrderedDict([
    #         ('organization', (u'Organization')),
    #         # ('groups', (u'Group')),
    #         ('tags', (u'Keyword')),

    #         ('res_format', (u'Format')),
    #         # ('accrualPeriodicity', _(u'Update frequency')),
    #         # ('datatype', _(u'Type')),
    #         # ('tags', _(u'Mot-clé')),
    #     ])

    # IFacets
    def dataset_facets(self, facets_dict, package_type):

        if package_type != 'dataset':
            return facets_dict

        return OrderedDict([('groups', 'Topics'),
                            #('vocab_category_all', 'Topic Categories'),
                            ('metadata_type', 'Dataset Type'),
                            ('tags', 'Tags'),
                            ('res_format', 'Formats'),
                            #('organization_type', 'Organization Types'),
                            ('organization', 'Organizations'),
                            ('publisher', 'Publishers'),
                            #('bureauCode', 'Bureaus'),
                            # ('extras_progress', 'Progress'),
                            ])

    def organization_facets(self, facets_dict, organization_type, package_type):

        if not package_type:
            return OrderedDict([('groups', 'Topics'),
                                #('vocab_category_all', 'Topic Categories'),
                                ('metadata_type', 'Dataset Type'),
                                ('tags', 'Tags'),
                                ('res_format', 'Formats'),
                                ('groups', 'Topics'),
                                #('harvest_source_title', 'Harvest Source'),
                                #('capacity', 'Visibility'),
                                #('dataset_type', 'Resource Type'),
                                #('publisher', 'Publishers'),
                                #('bureauCode', 'Bureaus'),
                                ])
        else:
            return facets_dict