
def flatten_dict(d):
    flat_dict = {}
    for key, value in d.items():
        if isinstance(value, dict):
            flat_dict.update(flatten_dict(value)) 
        else:
            flat_dict[key] = value
    return flat_dict

def rename_key(flat_dict, old_key, new_key):
    new_dict = {}
    for key, value in flat_dict.items():
        if key == old_key:
            new_dict[new_key] = value
        else:
            new_dict[key] = value           
    return new_dict


def process_new_ads(scraped_ad_data):

    ad_data = []
    for data in scraped_ad_data:
        ad_data.append(flatten_dict(data))

    processed_ad_data = []
    for data in ad_data:
        processed_ad_data.append(rename_key(data, "FINN-kode", "_id"))

    return processed_ad_data