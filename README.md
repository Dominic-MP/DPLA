# NAID/DPLA ID translator
===============

This is a set of two python scripts I made at the DPLAfest 2015 hackathon. They seek to solve the problem of finding the associated DPLA item ID for an ingested NARA catalog record using only the National Archives Identifier. Currently, you can find out a NAID for a given NARA record in DPLA using the DPLA API, but it's more difficult to go the other direction—since NARA's catalog does not store DPLA data, and you can't directly search by NAIDs in DPLA, because that field is just part of the originalRecord blob.

Using `NAIDtoDPLA.py`, you can enter a valid NAID which exists in DPLA, and it will return the DPLA item ID.

By contrast, `DPLAtoNAID.py` takes the approach of scanning over the entire set of NARA records in DPLA and making a CSV with a row for each NAID/DPLA item ID pair. There are currently 700,948 NARA records represented, so this takes a bit of time. The CSV output of this script (as of 4/22/2015) is also included in this repo.