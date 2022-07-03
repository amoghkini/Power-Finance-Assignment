from utils.Utils import Utils
import logging
class ProcessSearch:
    
    @staticmethod
    def processData(search, case, matchWholeWord):
        
        rdata = {}
        fileWordCountList = {}
        fileList = Utils.getFilesList()
        
        logging.info('processSearch: Going to search => %s', search)
        
        allFilesWordCount = 0
        
        for file in fileList:
            
            logging.info('processSearch: Searching in file => %s', file[63:])
            
            rdata[file[63:]]= []
            fileWordCountList[file[63:]] = []
            lineCount = 1
            fileWordCount = 0
            
            fh = open(file, 'r', encoding="utf8")
            fileLines = fh.readlines()

            for line in fileLines:
                lineList = line.split()
                if case == "Yes":
                    if matchWholeWord == "Yes":
                        if search in lineList:
                            allFilesWordCount += 1
                            fileWordCount += 1
                            rdata[file[63:]].append({lineCount:line.strip()})
                        lineCount += 1
                    else:
                        for word in lineList:
                            if word.find(search) == -1:
                                pass
                            else:
                                allFilesWordCount += 1
                                fileWordCount += 1
                                rdata[file[63:]].append({lineCount: line.strip()})
                                break
                        lineCount += 1
                else:
                    search = search.lower()
                    if matchWholeWord == "Yes":
                        if search in list(map(lambda x : x.lower(),lineList)):
                            allFilesWordCount += 1
                            fileWordCount += 1
                            rdata[file[63:]].append({lineCount: line.strip()})
                        lineCount += 1
                    else:
                        for word in lineList:
                            if word.lower().find(search) == -1:
                                pass
                            else:
                                allFilesWordCount += 1
                                fileWordCount += 1
                                rdata[file[63:]].append({lineCount: line.strip()})
                                break
                        lineCount += 1
                                        
            fileWordCountList[file[63:]] = fileWordCount
            logging.info('processSearch: Count of word "%s" is => %s', search, fileWordCount)
            
        logging.info('processSearch: Results %s',rdata)
        logging.info('processSearch: Count of word "%s" in all files is => %s',search, allFilesWordCount)
        
        return rdata, fileWordCountList, allFilesWordCount
    

        
