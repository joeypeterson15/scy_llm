import faiss
from sentence_transformers import SentenceTransformer
from pypdf import PdfReader
import numpy as np
import xml.etree.ElementTree as ET
from dicttoxml import dicttoxml


model = SentenceTransformer("all-MiniLM-L6-v2")
# reader = PdfReader('converted_document.pdf')
reader = PdfReader('griffiths EM.pdf')

def get_chunks(text, size=300, overlap=45):
    chunks = []
    for interval in range(0, len(text) - overlap, size):
        chunks.append(text[interval:(interval + size + overlap)])
    return chunks

text = ""
for page in reader.pages:
    text += page.extract_text()

chunks = get_chunks(text)

embeddings = model.encode(chunks)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings))


id_to_chunk = {i: chunk for i, chunk in enumerate(chunks)}
xml_bytes = dicttoxml(id_to_chunk, custom_root='data', attr_type=False)
xml_string = xml_bytes.decode('utf-8')
root = ET.Element(xml_string)
tree = ET.ElementTree(root)
tree.write('id_to_chunk.xml', encoding='UTF-8')

path = "./my_faiss_index.index"
faiss.write_index(index, path)
