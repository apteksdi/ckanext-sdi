from collections import OrderedDict
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

def most_recent_datasets(num=3):
        datasets = toolkit.get_action('package_search')({}, {'sort': 'metadata_modified desc',
                                                        'fq': 'private:false',
                                                        'rows': num})
        return datasets.get('results', [])

def dataset_count():
    """Return a count of all datasets"""

    result = toolkit.get_action('package_search')({}, {'rows': 1})
    return result['count']

def groups():
    """Return a list of groups"""

    return toolkit.get_action('group_list')({}, {'all_fields': True})

def package_showcase_list(context):
    return toolkit.get_action('ckanext_package_showcase_list')({}, {'package_id': context.pkg_dict['id']})

def ckan_site_url():
    return config.get('ckan.site_url', '').rstrip('/')

#package_extra
def get_pkg_dict_extra(pkg_dict, key, default=None):
    '''Override the CKAN core helper to add rolled up extras
    Returns the value for the dataset extra with the provided key.

    If the key is not found, it returns a default value, which is None by
    default.

    :param pkg_dict: dictized dataset
    :key: extra key to lookup
    :default: default value returned if not found
    '''
    extras = pkg_dict['extras'] if 'extras' in pkg_dict else []

    for extra in extras:
        if extra['key'] == key:
            return extra['value']

    # also include the rolled up extras
    for extra in extras:
        if 'extras_rollup' == extra.get('key'):
            rolledup_extras = json.loads(extra.get('value'))
            for k, value in rolledup_extras.items():
                if k == key:
                    return value

class SDIPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IFacets, inherit=True)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'sdi')

    # IFacets
    def dataset_facets(self, facets_dict, package_type):

        if package_type != 'dataset':
            return facets_dict

        return OrderedDict([('kategori', 'Kategori'),
                            ('prioritas_tahun', 'Data Prioritas'),
                            #('groups', 'Grup'),
                            ('organization', 'Walidata'),
                            #('vocab_category_all', 'Topic Categories'),
                            #('metadata_type', 'Dataset Type'),
                            #('tags', 'Tagging'),
                            ('res_format', 'Format'),
                            #('organization_type', 'Organization Types'),
                            #('publisher', 'Publishers'),
                            #('extras_progress', 'Progress'),
                            ])

    def organization_facets(self, facets_dict, organization_type, package_type):

        if not package_type:
            return OrderedDict([('organization', 'Walidata'),
                                ('kategori', 'Kategori'),
                                ('prioritas_tahun', 'Data Prioritas'),
                                #('groups', 'Grup'),
                                #('organization', 'Instansi'),
                                #('vocab_category_all', 'Topic Categories'),
                                #('metadata_type', 'Dataset Type'),
                                #('tags', 'Tagging'),
                                ('res_format', 'Format'),
                                #('harvest_source_title', 'Harvest Source'),
                                #('capacity', 'Visibility'),
                                #('dataset_type', 'Resource Type'),
                                #('publisher', 'Publishers'),
                                ])
        else:
            return facets_dict

    def group_facets(self, facets_dict, group_type, package_type):

        # get the categories key
        group_id = plugins.toolkit.c.group_dict['id']
        key = 'vocab___category_tag_%s' % group_id
        if not package_type:
            return OrderedDict([('kategori', 'Kategori'),
                                ('prioritas_tahun', 'Data Prioritas'),
                                #('groups', 'Grup'),
                                ('organization', 'Walidata'),
                                #('metadata_type', 'Dataset Type'),
                                #('organization_type', 'Organization Types'),
                                #('tags', 'Tagging'),
                                ('res_format', 'Format'),
                                #(key, 'Categories'),
                                #('publisher', 'Publisher'),
                                ])
        else:
            return facets_dict

    def get_helpers(self):
        """Register sdbi_theme_* helper functions"""

        return {'sdi_theme_most_recent_datasets': most_recent_datasets,
                'sdi_theme_dataset_count': dataset_count,
                'sdi_theme_groups': groups,
                'ckan_site_url': ckan_site_url,
                'get_pkg_dict_extra': get_pkg_dict_extra,
                'package_showcase_list': package_showcase_list}
