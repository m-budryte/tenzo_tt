class String_processor:
    def remove_first_line(self, full_string):
        return '\n'.join(full_string.split('\n')[1:])

    def split_into_entries(self, full_string):
        extracted_data = self.remove_first_line(full_string)
        return extracted_data.split("\n")

    def split_entry(self, entry):
        return entry.split(",")

    def process_string(self, full_string):
        entries = self.split_into_entries(full_string)
        processed_entries = [self.split_entry(entry) for entry in entries]
        return processed_entries
