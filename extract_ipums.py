from ipumspy import IpumsApiClient, AggregateDataExtract, NhgisDataset
from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

IPUMS_API_KEY = os.environ.get("API_KEY")
ipums = IpumsApiClient(IPUMS_API_KEY)

# Create an extract
extract = AggregateDataExtract(
   collection="nhgis",
   description="2000 Census Race",
   datasets=[
      NhgisDataset(name="2000_SF2", data_tables=['NPCT001A'], geog_levels=["tract"])
   ]
)

ipums.submit_extract(extract)
ipums.wait_for_extract(extract)

DOWNLOAD_DIR = Path(Path.cwd() / "data/")
ipums.download_extract(extract, download_dir=DOWNLOAD_DIR)