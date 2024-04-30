
def output_processing(output):
    entity_group_mapping = {
    "PER": "Person",
    "LOC": "Location",
    "ORG": "Orangization"
}

    combined_data = {}
    for item in data:
        entity_group = item['entity_group']
        word = item['word']
        full_entity_group = entity_group_mapping.get(entity_group, entity_group)
        if full_entity_group in combined_data:
            combined_data[full_entity_group].append(word)
        else:
            combined_data[full_entity_group] = [word]

    return combined_data