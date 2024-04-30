
def output_processing(data):
    entity_group_mapping = {
    "B-PER": "Person",
    "B-LOC": "Location",
    "B-ORG": "Organization"}

    combined_data = {}
    for item in data:
        entity_group = item['entity']
        word = item['word']
        full_entity_group = entity_group_mapping.get(entity_group, entity_group)
        if full_entity_group in combined_data:
            combined_data[full_entity_group].append(word)
        else:
            combined_data[full_entity_group] = [word]

    return combined_data