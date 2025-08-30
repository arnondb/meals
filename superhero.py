letter_attribute = [
	"דולפינים",
		"תחתונים",
			"ברווזי האש",
				"דרקונים",
					"נמרים",
					"מחשבים",
						"H2O",
						"חתולים",
						"מוזיקה",
							"אש",
								"",
							"אופנועים"
								"",
								"גלקסיה",
									"",
									"בנות הים",
										"",
										"שמש",
										"נחשים",
											"קסמים",
											"",
												"פרפרי הפרא",
												"",
													"אריות",
														"לילה",
															"חורים שחורים",
																"פלאטיפוסים",
																	"חלליות"]
class superhero:
	def __init__(self, letter):
		self.hebrew_index = ord(letter[0:1]) - 1488
		self.att_letter = letter_attribute[self.hebrew_index]
 
name = input('אנא כתוב את שמך  ')
s1 = superhero(name)
print("היכולת שלך היא:", s1.att_letter)
