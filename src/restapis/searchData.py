import logging
from flask.views import MethodView
from flask import render_template
from flaskforms.searchForm import searchForm
from core.processSearch import ProcessSearch
import time
class searchData(MethodView):
    
    def get(self):
        form = searchForm()
        return render_template('index.html',form=form)
    
    def post(self):
        form = searchForm()
        
        search = form.searchName.data
        case = form.caseSensitive.data
        matchWholeWord = form.matchWholeWord.data
        
        start_time = time.time()
        result, fileWordCountList, allFilesWordCount = ProcessSearch.processData(search,case,matchWholeWord)
        end_time = time.time()
        
        logging.info("searchData: Processing time taken ==> %s",(end_time-start_time))
        
        if allFilesWordCount > 0:
            returnPayload = {"Payload": result, "AllFilesWordCount": allFilesWordCount, "fileWordCountList": fileWordCountList}
        else:
            returnPayload = {"Payload":None}
            
        #return returnPayload
        return render_template('index.html',form=form,returnPayload=returnPayload)
        
    
