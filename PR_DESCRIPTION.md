# Pretty-Print JSON Export Output

## Summary
This PR improves the JSON export functionality by formatting the output with proper indentation and readability. Previously, the JSON was displayed as a minified string, making it difficult to read and understand.

## Changes Made
- Added `json` import to `src/ui/base_xml_window.py`
- Updated `export_to_json()` method to use `json.dumps()` with formatting parameters instead of `str()` conversion

## Technical Details
- **File Modified**: `src/ui/base_xml_window.py`
- **Line 4**: Added `import json`
- **Line 452**: Changed from `str(self.output_text)` to `json.dumps(self.output_text, indent=2, ensure_ascii=False)`

The `indent=2` parameter adds 2-space indentation for hierarchical readability, and `ensure_ascii=False` ensures proper display of Unicode characters (e.g., Arabic text, emojis).

## Impact
- **Before**: JSON output was displayed as a single minified line: `{'users': [{'id': '1', 'name': 'John', ...}]}`
- **After**: JSON output is properly formatted with indentation:
  ```json
  {
    "users": [
      {
        "id": "1",
        "name": "John",
        ...
      }
    ]
  }
  ```

## Testing
1. Launch the application: `python app_main.py`
2. Load an XML file (Browse or Manual mode)
3. Click the "📄 Export to JSON" button
4. Verify that the JSON in the result text box is properly formatted with indentation and line breaks

## Screenshots
_Add screenshots showing before/after comparison if available_
