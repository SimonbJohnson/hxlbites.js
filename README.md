

# hxlbites.js

hxlbites.js is a library to automate the generation of the relevant and context aware data structures for charts, maps, tables and text of humanitarian data with HXL hastags.

Usage:

Data should be an array of arrays - first line = headers, second line = hxl hashtags, third line onwards = data

<blockquote>var hb = hxbites.data(data)</blockquote>

To get mapping bites
<blockquote>hb.getMapBites();</blockquote>

return array of bites with following structure:

{  
  bite: array [...data for chart...],  
  geom_attribute: string "...field name in geometry file to join data by...",  
  geom_url: array [...URLs to download matchin geometry file],  
  id: string "...chart bite ID...",  
  priority: number,  
  subtype: string "...bite subtype - choropleth...",  
  title: string "...title of bite...",  
  type: string "...bite type...",  
  uniqueID: string "...unique ID combining bite and data structure...",  
}  

To get chart bites
<blockquote>hb.getChartBites();</blockquote>

return array of bites with following structure:

{  
  bite: array [...data for chart...],  
  id: string "...chart bite ID...",  
  priority: number,  
  subtype: string "...bite subtype - row, pie...",  
  title: string "...title of bite...",  
  type: string "...bite type...",  
  uniqueID: string "...unique ID combining bite and data structure",  
}  

To get table bites
<blockquote>hb.getTableBites();</blockquote>

To get crosstable bites
<blockquote>hb.getCrosstableBites();</blockquote>

To get text bites
<blockquote>hb.getTextBites();</blockquote>

{
  bite: string "...generate text string...",  
  id: string "...chart bite ID...",  
  priority: number,  
  subtype: string "...bite subtype - main, headline figure...",  
  title: undefined,  
  type: string "...bite type...",  
  uniqueID: string "...unique ID combining bite and data structure",  
}

<blockquote>hb.reverse(uniqueID)</blockquote>
Return single bite related to unique ID.  Data does not have to be the same and makes best attempt to recreate bite with new numbers.
