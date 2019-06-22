mdp

const int TL_RED = 0;
const int TL_GREEN = 1;
const int TL_ORANGE = 2;

const bool PB_DEACTIVATE = false;
const bool PB_ACTIVATE = true;

const bool YES = true;
const bool NO = false;

const int PHASE_DEACTIVATE=0;
const int PHASE_ORANGE=1;
const int PHASE_RED=2;
const int PHASE_GREEN=3;
const int PHASE_FINISH=4;


module phase_1
	s_phase_1: [0..5] init PHASE_ORANGE;
	[p3_finish] s_phase_1=PHASE_DEACTIVATE & s_phase_3=PHASE_FINISH & !s_pb2 & !(s_pb1 & s_pb3) & !s_fire -> (s_phase_1'=PHASE_ORANGE);
	[p3_finish] s_phase_1=PHASE_DEACTIVATE & s_phase_3=PHASE_FINISH & (s_pb2 | (s_pb1 & s_pb3)) | s_fire -> (s_phase_1'=PHASE_DEACTIVATE);
	
	[p6_finish] s_phase_1=PHASE_DEACTIVATE & s_phase_6=PHASE_FINISH & !s_pb2 & !s_fire -> (s_phase_1'=PHASE_ORANGE);
	[p6_finish] s_phase_1=PHASE_DEACTIVATE & s_phase_6=PHASE_FINISH & s_pb2 | s_fire-> (s_phase_1'=PHASE_DEACTIVATE);

	[p8_3_finish] s_phase_3=PHASE_DEACTIVATE & s_phase_8_3=PHASE_FINISH & !s_pb2  -> (s_phase_1'=PHASE_ORANGE);
	[p8_3_finish] s_phase_3=PHASE_DEACTIVATE & s_phase_8_3=PHASE_FINISH & s_pb2 -> (s_phase_1'=PHASE_DEACTIVATE);

	[p7_3_finish] s_phase_1=PHASE_DEACTIVATE & s_phase_7_3=PHASE_FINISH & !s_fire-> (s_phase_1'=PHASE_ORANGE);
	[p7_3_finish] s_phase_1=PHASE_DEACTIVATE & s_phase_7_3=PHASE_FINISH & s_fire-> (s_phase_1'=PHASE_DEACTIVATE);

	[p1_red] s_phase_1=PHASE_ORANGE -> (s_phase_1'=PHASE_RED);
	[p1_green] s_phase_1=PHASE_RED -> (s_phase_1'=PHASE_GREEN);
	[] s_phase_1=PHASE_GREEN -> (s_phase_1'=PHASE_FINISH);
	[p1_finish] s_phase_1=PHASE_FINISH -> (s_phase_1'=PHASE_DEACTIVATE);
endmodule

module phase_2
	s_phase_2: [0..5] init PHASE_DEACTIVATE;
	[p1_finish] s_phase_2=PHASE_DEACTIVATE & s_phase_1=PHASE_FINISH & !s_pb3 & !(s_pb2 & s_pb1) & !s_fire-> (s_phase_2'=PHASE_ORANGE);
	[p1_finish] s_phase_2=PHASE_DEACTIVATE & s_phase_1=PHASE_FINISH & (s_pb3 | (s_pb2 & s_pb1)) | s_fire-> (s_phase_2'=PHASE_DEACTIVATE);

	[p8_1_finish] s_phase_2=PHASE_DEACTIVATE & s_phase_8_1=PHASE_FINISH & !s_pb3  -> (s_phase_2'=PHASE_ORANGE);
	[p8_1_finish] s_phase_2=PHASE_DEACTIVATE & s_phase_8_1=PHASE_FINISH & s_pb3 -> (s_phase_2'=PHASE_DEACTIVATE);

	[p4_finish] s_phase_2=PHASE_DEACTIVATE & s_phase_4=PHASE_FINISH & !s_pb3 & !s_fire-> (s_phase_2'=PHASE_ORANGE);
	[p4_finish] s_phase_2=PHASE_DEACTIVATE & s_phase_4=PHASE_FINISH & s_pb3 | s_fire-> (s_phase_2'=PHASE_DEACTIVATE);

	[p7_1_finish] s_phase_2=PHASE_DEACTIVATE & s_phase_7_1=PHASE_FINISH & !s_fire-> (s_phase_2'=PHASE_ORANGE);
	[p7_1_finish] s_phase_2=PHASE_DEACTIVATE & s_phase_7_1=PHASE_FINISH & s_fire-> (s_phase_2'=PHASE_DEACTIVATE);

	[p2_red] s_phase_2=PHASE_ORANGE -> (s_phase_2'=PHASE_RED);
	[p2_green] s_phase_2=PHASE_RED -> (s_phase_2'=PHASE_GREEN);
	[] s_phase_2=PHASE_GREEN -> (s_phase_2'=PHASE_FINISH);
	[p2_finish] s_phase_2=PHASE_FINISH -> (s_phase_2'=PHASE_DEACTIVATE);
endmodule

module phase_3
	s_phase_3: [0..5] init PHASE_DEACTIVATE;
	[p2_finish] s_phase_3=PHASE_DEACTIVATE & s_phase_2=PHASE_FINISH & !s_pb1 & !(s_pb2 & s_pb3) & !s_fire-> (s_phase_3'=PHASE_ORANGE);
	[p2_finish] s_phase_3=PHASE_DEACTIVATE & s_phase_2=PHASE_FINISH & (s_pb1 | (s_pb2 & s_pb3)) | s_fire -> (s_phase_3'=PHASE_DEACTIVATE);

	[p5_finish] s_phase_3=PHASE_DEACTIVATE & s_phase_5=PHASE_FINISH & !s_pb1 & !s_fire-> (s_phase_3'=PHASE_ORANGE);
	[p5_finish] s_phase_3=PHASE_DEACTIVATE & s_phase_5=PHASE_FINISH & s_pb1 | s_fire-> (s_phase_3'=PHASE_DEACTIVATE);

	[p8_2_finish] s_phase_3=PHASE_DEACTIVATE & s_phase_8_2=PHASE_FINISH & !s_pb1 -> (s_phase_3'=PHASE_ORANGE);
	[p8_2_finish] s_phase_3=PHASE_DEACTIVATE & s_phase_8_2=PHASE_FINISH & s_pb1 -> (s_phase_3'=PHASE_DEACTIVATE);

	[p7_2_finish] s_phase_3=PHASE_DEACTIVATE & s_phase_7_2=PHASE_FINISH & !s_fire -> (s_phase_3'=PHASE_ORANGE);	
	[p7_2_finish] s_phase_3=PHASE_DEACTIVATE & s_phase_7_2=PHASE_FINISH & s_fire -> (s_phase_3'=PHASE_DEACTIVATE);	

	[p3_red] s_phase_3=PHASE_ORANGE -> (s_phase_3'=PHASE_RED);
	[p3_green] s_phase_3=PHASE_RED -> (s_phase_3'=PHASE_GREEN);
	[] s_phase_3=PHASE_GREEN -> (s_phase_3'=PHASE_FINISH);
	[p3_finish] s_phase_3=PHASE_FINISH -> (s_phase_3'=PHASE_DEACTIVATE);
endmodule 

module phase_4
	s_phase_4: [0..5] init PHASE_DEACTIVATE;
	[p3_finish] s_phase_4=PHASE_DEACTIVATE & s_phase_3=PHASE_FINISH & s_pb2 & (!s_pb1 & !s_pb3) & !s_fire-> (s_phase_4'=PHASE_ORANGE);
	[p3_finish] s_phase_4=PHASE_DEACTIVATE & s_phase_3=PHASE_FINISH & (!s_pb2 | (s_pb1 | s_pb3)) | s_fire-> (s_phase_4'=PHASE_DEACTIVATE);

	[p6_finish] s_phase_4=PHASE_DEACTIVATE & s_phase_6=PHASE_FINISH & s_pb2 & !s_pb3 & !s_fire-> (s_phase_4'=PHASE_ORANGE);
	[p6_finish] s_phase_4=PHASE_DEACTIVATE & s_phase_6=PHASE_FINISH & (!s_pb2 | (s_pb2 & s_pb3)) | s_fire-> (s_phase_4'=PHASE_DEACTIVATE);

	[p8_3_finish] s_phase_4=PHASE_DEACTIVATE & s_phase_8_3=PHASE_FINISH & s_pb2  -> (s_phase_4'=PHASE_ORANGE);
	[p8_3_finish] s_phase_4=PHASE_DEACTIVATE & s_phase_8_3=PHASE_FINISH & !s_pb2 -> (s_phase_4'=PHASE_DEACTIVATE);

	[p4_red] s_phase_4=PHASE_ORANGE -> (s_phase_4'=PHASE_RED);
	[p4_green] s_phase_4=PHASE_RED -> (s_phase_4'=PHASE_GREEN);
	[] s_phase_4=PHASE_GREEN -> (s_phase_4'=PHASE_FINISH);
	[p4_finish] s_phase_4=PHASE_FINISH -> (s_phase_4'=PHASE_DEACTIVATE);
endmodule 

module phase_5
	s_phase_5: [0..5] init PHASE_DEACTIVATE;
	[p1_finish] s_phase_5=PHASE_DEACTIVATE & s_phase_1=PHASE_FINISH & s_pb3 & (!s_pb2 & !s_pb1) & !s_fire-> (s_phase_5'=PHASE_ORANGE);
	[p1_finish] s_phase_5=PHASE_DEACTIVATE & s_phase_1=PHASE_FINISH & !s_pb3 | (s_pb1 | s_pb2) | s_fire-> (s_phase_5'=PHASE_DEACTIVATE);

	[p8_1_finish] s_phase_5=PHASE_DEACTIVATE & s_phase_8_1=PHASE_FINISH & s_pb3 -> (s_phase_5'=PHASE_ORANGE);
	[p8_1_finish] s_phase_5=PHASE_DEACTIVATE & s_phase_8_1=PHASE_FINISH & !s_pb3 -> (s_phase_5'=PHASE_DEACTIVATE);

	[p4_finish] s_phase_5=PHASE_DEACTIVATE & s_phase_4=PHASE_FINISH & s_pb3 & !s_pb1 & !s_fire -> (s_phase_5'=PHASE_ORANGE);
	[p4_finish] s_phase_5=PHASE_DEACTIVATE & s_phase_4=PHASE_FINISH & (!s_pb3 | (s_pb3 & s_pb1)) | s_fire -> (s_phase_5'=PHASE_DEACTIVATE);

	[p5_red] s_phase_5=PHASE_ORANGE -> (s_phase_5'=PHASE_RED);
	[p5_green] s_phase_5=PHASE_RED -> (s_phase_5'=PHASE_GREEN);
	[] s_phase_5=PHASE_GREEN -> (s_phase_5'=PHASE_FINISH);
	[p5_finish] s_phase_5=PHASE_FINISH -> (s_phase_5'=PHASE_DEACTIVATE);
endmodule

module phase_6
	// TODO
	s_phase_6: [0..5] init PHASE_DEACTIVATE;
	[p2_finish] s_phase_6=PHASE_DEACTIVATE & s_phase_2=PHASE_FINISH & s_pb1 & (!s_pb2 & !s_pb3) & !s_fire -> (s_phase_6'=PHASE_ORANGE);
	[p2_finish] s_phase_6=PHASE_DEACTIVATE & s_phase_2=PHASE_FINISH & !s_pb1 | (s_pb2 | s_pb3) | s_fire  -> (s_phase_6'=PHASE_DEACTIVATE);
	// juste !s_pb1 pas suffisant car si on a les 3 pb activées, ici on rentrerait dans aucun des cas

	[p5_finish] s_phase_6=PHASE_DEACTIVATE & s_phase_5=PHASE_FINISH & s_pb1 & !s_pb2 & !s_fire -> (s_phase_6'=PHASE_ORANGE);
	[p5_finish] s_phase_6=PHASE_DEACTIVATE & s_phase_5=PHASE_FINISH & !s_pb1 | s_fire | (s_pb1 & s_pb2) -> (s_phase_6'=PHASE_DEACTIVATE);

	[p8_2_finish] s_phase_6=PHASE_DEACTIVATE & s_phase_8_2=PHASE_FINISH & s_pb1 -> (s_phase_6'=PHASE_ORANGE);
	[p8_2_finish] s_phase_6=PHASE_DEACTIVATE & s_phase_8_2=PHASE_FINISH & !s_pb1 -> (s_phase_6'=PHASE_DEACTIVATE);

	[p6_red] s_phase_6=PHASE_ORANGE -> (s_phase_6'=PHASE_RED);
	[p6_green] s_phase_6=PHASE_RED -> (s_phase_6'=PHASE_GREEN);
	[] s_phase_6=PHASE_GREEN -> (s_phase_6'=PHASE_FINISH);
	[p6_finish] s_phase_6=PHASE_FINISH -> (s_phase_6'=PHASE_DEACTIVATE);
endmodule 

module phase_7_1
	s_phase_7_1: [0..5] init PHASE_DEACTIVATE;
	
	[p1_finish] s_phase_7_1=PHASE_DEACTIVATE & s_phase_1=PHASE_FINISH & ((s_pb1 & s_pb2) | (s_pb2 & s_pb3) | (s_pb1 & s_pb3)) & !s_fire-> (s_phase_7_1'=PHASE_ORANGE);
	[p1_finish] s_phase_7_1=PHASE_DEACTIVATE & s_phase_1=PHASE_FINISH & (!s_pb1 & !s_pb2 & !s_pb3) | s_fire -> (s_phase_7_1'=PHASE_DEACTIVATE);
	[p1_finish] s_phase_7_1=PHASE_DEACTIVATE & s_phase_1=PHASE_FINISH & (s_pb1 & (!s_pb2 & !s_pb3)) | (s_pb2 & (!s_pb1 & !s_pb3)) 
	| (s_pb3 & (!s_pb1 & !s_pb2)) | s_fire -> (s_phase_7_1'=PHASE_DEACTIVATE);
	
	[p4_finish] s_phase_7_1=PHASE_DEACTIVATE & s_phase_4=PHASE_FINISH & (s_pb1 & s_pb3) & !s_fire -> (s_phase_7_1'=PHASE_ORANGE);
	[p4_finish] s_phase_7_1=PHASE_DEACTIVATE & s_phase_4=PHASE_FINISH & !(s_pb1 & s_pb3) | s_fire -> (s_phase_7_1'=PHASE_DEACTIVATE);
	[p7_1_red] s_phase_7_1=PHASE_ORANGE -> (s_phase_7_1'=PHASE_RED);
	[p7_1_green] s_phase_7_1=PHASE_RED -> (s_phase_7_1'=PHASE_GREEN);
	[] s_phase_7_1=PHASE_GREEN -> (s_phase_7_1'=PHASE_FINISH);
	[p7_1_finish] s_phase_7_1=PHASE_FINISH -> (s_phase_7_1'=PHASE_DEACTIVATE);
endmodule 

module phase_7_2
	s_phase_7_2: [0..5] init PHASE_DEACTIVATE;
	
	[p2_finish] s_phase_7_2=PHASE_DEACTIVATE & s_phase_2=PHASE_FINISH & ((s_pb1 & s_pb2) | (s_pb2 & s_pb3) | (s_pb1 & s_pb3)) & !s_fire -> (s_phase_7_2'=PHASE_ORANGE);
	[p2_finish] s_phase_7_2=PHASE_DEACTIVATE & s_phase_2=PHASE_FINISH & (!s_pb1 & !s_pb2 & !s_pb3) | s_fire -> (s_phase_7_2'=PHASE_DEACTIVATE);
	[p2_finish] s_phase_7_2=PHASE_DEACTIVATE & s_phase_2=PHASE_FINISH & (s_pb1 & (!s_pb2 & !s_pb3)) | (s_pb2 & (!s_pb1 & !s_pb3)) 
	| (s_pb3 & (!s_pb1 & !s_pb2)) | s_fire -> (s_phase_7_2'=PHASE_DEACTIVATE);

	[p5_finish] s_phase_7_2=PHASE_DEACTIVATE & s_phase_5=PHASE_FINISH & (s_pb1 & s_pb2) & !s_fire-> (s_phase_7_2'=PHASE_ORANGE);
	[p5_finish] s_phase_7_2=PHASE_DEACTIVATE & s_phase_5=PHASE_FINISH & !(s_pb1 & s_pb2) | s_fire-> (s_phase_7_2'=PHASE_DEACTIVATE);
	[p7_2_red] s_phase_7_2=PHASE_ORANGE -> (s_phase_7_2'=PHASE_RED);
	[p7_2_green] s_phase_7_2=PHASE_RED -> (s_phase_7_2'=PHASE_GREEN);
	[] s_phase_7_2=PHASE_GREEN -> (s_phase_7_2'=PHASE_FINISH);
	[p7_2_finish] s_phase_7_2=PHASE_FINISH -> (s_phase_7_2'=PHASE_DEACTIVATE);
endmodule 

module phase_7_3
	s_phase_7_3: [0..5] init PHASE_DEACTIVATE;
	
	[p3_finish] s_phase_7_3=PHASE_DEACTIVATE & s_phase_3=PHASE_FINISH & ((s_pb1 & s_pb2) | (s_pb2 & s_pb3) | (s_pb1 & s_pb3)) & !s_fire-> (s_phase_7_3'=PHASE_ORANGE);
	[p3_finish] s_phase_7_3=PHASE_DEACTIVATE & s_phase_3=PHASE_FINISH & (!s_pb1 & !s_pb2 & !s_pb3) | s_fire-> (s_phase_7_3'=PHASE_DEACTIVATE);
	[p3_finish] s_phase_7_3=PHASE_DEACTIVATE & s_phase_3=PHASE_FINISH & (s_pb1 & (!s_pb2 & !s_pb3)) | (s_pb2 & (!s_pb1 & !s_pb3)) 
	| (s_pb3 & (!s_pb1 & !s_pb2)) | s_fire -> (s_phase_7_3'=PHASE_DEACTIVATE);
	
	[p6_finish] s_phase_7_3=PHASE_DEACTIVATE & s_phase_6=PHASE_FINISH & (s_pb2 & s_pb3) & !s_fire -> (s_phase_7_3'=PHASE_ORANGE);
	[p6_finish] s_phase_7_3=PHASE_DEACTIVATE & s_phase_6=PHASE_FINISH & !(s_pb2 & s_pb3) | s_fire-> (s_phase_7_3'=PHASE_DEACTIVATE);
	[p7_3_red] s_phase_7_3=PHASE_ORANGE -> (s_phase_7_3'=PHASE_RED);
	[p7_3_green] s_phase_7_3=PHASE_RED -> (s_phase_7_3'=PHASE_GREEN);
	[] s_phase_7_3=PHASE_GREEN -> (s_phase_7_3'=PHASE_FINISH);
	[p7_3_finish] s_phase_7_3=PHASE_FINISH -> (s_phase_7_3'=PHASE_DEACTIVATE);
endmodule

module phase_8_1
	s_phase_8_1: [0..5] init PHASE_DEACTIVATE;
	
	[p1_finish] s_phase_8_1=PHASE_DEACTIVATE & s_phase_1=PHASE_FINISH & s_fire-> (s_phase_8_1'=PHASE_ORANGE);
	[p1_finish] s_phase_8_1=PHASE_DEACTIVATE & s_phase_1=PHASE_FINISH & !s_fire -> (s_phase_8_1'=PHASE_DEACTIVATE);
	[p4_finish] s_phase_8_1=PHASE_DEACTIVATE & s_phase_4=PHASE_FINISH & s_fire -> (s_phase_8_1'=PHASE_ORANGE);
	[p4_finish] s_phase_8_1=PHASE_DEACTIVATE & s_phase_4=PHASE_FINISH & !s_fire -> (s_phase_8_1'=PHASE_DEACTIVATE);

	[p7_1_finish] s_phase_8_1=PHASE_DEACTIVATE & s_phase_7_1=PHASE_FINISH & s_fire -> (s_phase_8_1'=PHASE_ORANGE);
	[p7_1_finish] s_phase_8_1=PHASE_DEACTIVATE & s_phase_7_1=PHASE_FINISH & !s_fire -> (s_phase_8_1'=PHASE_DEACTIVATE);
	
	[p8_1_red] s_phase_8_1=PHASE_ORANGE -> (s_phase_8_1'=PHASE_RED);
	[p8_1_green] s_phase_8_1=PHASE_RED -> (s_phase_8_1'=PHASE_GREEN);
	[] s_phase_8_1=PHASE_GREEN -> (s_phase_8_1'=PHASE_FINISH);
	[p8_1_finish] s_phase_8_1=PHASE_FINISH -> (s_phase_8_1'=PHASE_DEACTIVATE);
endmodule

module phase_8_2
	s_phase_8_2: [0..5] init PHASE_DEACTIVATE;
	
	[p2_finish] s_phase_8_2=PHASE_DEACTIVATE & s_phase_2=PHASE_FINISH & s_fire-> (s_phase_8_2'=PHASE_ORANGE);
	[p2_finish] s_phase_8_2=PHASE_DEACTIVATE & s_phase_2=PHASE_FINISH & !s_fire -> (s_phase_8_2'=PHASE_DEACTIVATE);
	[p5_finish] s_phase_8_2=PHASE_DEACTIVATE & s_phase_5=PHASE_FINISH & s_fire -> (s_phase_8_2'=PHASE_ORANGE);
	[p5_finish] s_phase_8_2=PHASE_DEACTIVATE & s_phase_5=PHASE_FINISH & !s_fire -> (s_phase_8_2'=PHASE_DEACTIVATE);


	[p7_2_finish] s_phase_8_2=PHASE_DEACTIVATE & s_phase_7_2=PHASE_FINISH & s_fire -> (s_phase_8_2'=PHASE_ORANGE);
	[p7_2_finish] s_phase_8_2=PHASE_DEACTIVATE & s_phase_7_2=PHASE_FINISH & !s_fire -> (s_phase_8_2'=PHASE_DEACTIVATE);
	
	[p8_2_red] s_phase_8_2=PHASE_ORANGE -> (s_phase_8_2'=PHASE_RED);
	[p8_2_green] s_phase_8_2=PHASE_RED -> (s_phase_8_2'=PHASE_GREEN);
	[] s_phase_8_2=PHASE_GREEN -> (s_phase_8_2'=PHASE_FINISH);
	[p8_2_finish] s_phase_8_2=PHASE_FINISH -> (s_phase_8_2'=PHASE_DEACTIVATE);
endmodule

module phase_8_3
	s_phase_8_3: [0..5] init PHASE_DEACTIVATE;
	
	[p3_finish] s_phase_8_3=PHASE_DEACTIVATE & s_phase_3=PHASE_FINISH & s_fire-> (s_phase_8_3'=PHASE_ORANGE);
	[p3_finish] s_phase_8_3=PHASE_DEACTIVATE & s_phase_3=PHASE_FINISH & !s_fire -> (s_phase_8_3'=PHASE_DEACTIVATE);
	[p6_finish] s_phase_8_3=PHASE_DEACTIVATE & s_phase_6=PHASE_FINISH & s_fire -> (s_phase_8_3'=PHASE_ORANGE);
	[p6_finish] s_phase_8_2=PHASE_DEACTIVATE & s_phase_6=PHASE_FINISH & !s_fire -> (s_phase_8_3'=PHASE_DEACTIVATE);

	[p7_3_finish] s_phase_8_3=PHASE_DEACTIVATE & s_phase_7_3=PHASE_FINISH & s_fire -> (s_phase_8_3'=PHASE_ORANGE);
	[p7_3_finish] s_phase_8_3=PHASE_DEACTIVATE & s_phase_7_3=PHASE_FINISH & !s_fire -> (s_phase_8_3'=PHASE_DEACTIVATE);
	
	[p8_3_red] s_phase_8_3=PHASE_ORANGE -> (s_phase_8_3'=PHASE_RED);
	[p8_3_green] s_phase_8_3=PHASE_RED -> (s_phase_8_3'=PHASE_GREEN);
	[] s_phase_8_3=PHASE_GREEN -> (s_phase_8_3'=PHASE_FINISH);
	[p8_3_finish] s_phase_8_3=PHASE_FINISH -> (s_phase_8_3'=PHASE_DEACTIVATE);
endmodule



module tl1
	// TODO
	s_tl1: [0..2] init TL_RED;
	[p3_red] s_tl1=TL_RED -> (s_tl1'=TL_RED);
	[p3_red] s_tl1=TL_GREEN -> (s_tl1'=TL_RED);
	
	[p2_green] s_tl1=TL_RED -> (s_tl1'=TL_GREEN);

	[p5_green] s_tl1=TL_RED -> (s_tl1'=TL_GREEN);

	[p6_red] s_tl1=TL_RED -> (s_tl1'=TL_RED);
	[p6_red] s_tl1=TL_GREEN -> (s_tl1'=TL_RED);

	[p7_2_red] s_tl1=TL_GREEN -> (s_tl1'=TL_RED);

	[p8_2_red] s_tl1=TL_RED -> (s_tl1'=TL_RED);
	[p8_2_red] s_tl1=TL_GREEN -> (s_tl1'=TL_RED);
endmodule

module tl2
	// TODO
	s_tl2: [0..2] init TL_RED;
	[p1_green] s_tl2=TL_RED -> (s_tl2'=TL_GREEN);
	[p1_green] s_tl2=TL_GREEN -> (s_tl2'=TL_GREEN);

	[p2_green] s_tl2=TL_GREEN -> (s_tl2'=TL_GREEN);		
	[p2_green] s_tl2=TL_RED -> (s_tl2'=TL_GREEN);

	[p3_green] s_tl2=TL_GREEN -> (s_tl2'=TL_GREEN);		
	[p3_green] s_tl2=TL_RED -> (s_tl2'=TL_GREEN);

	[p4_green] s_tl2=TL_GREEN -> (s_tl2'=TL_GREEN);		
	[p4_green] s_tl2=TL_RED -> (s_tl2'=TL_GREEN);

	[p5_red] s_tl2=TL_GREEN -> (s_tl2'=TL_RED);		
	[p5_red] s_tl2=TL_RED -> (s_tl2'=TL_RED);

	[p6_red] s_tl2=TL_GREEN -> (s_tl2'=TL_RED);		
	[p6_red] s_tl2=TL_RED -> (s_tl2'=TL_RED);

	[p7_1_red] s_tl2=TL_GREEN -> (s_tl2'=TL_RED);

	[p7_2_red] s_tl2=TL_GREEN -> (s_tl2'=TL_RED);		
	[p7_2_red] s_tl2=TL_RED -> (s_tl2'=TL_RED);

	[p7_3_red] s_tl2=TL_GREEN -> (s_tl2'=TL_RED);		
	[p7_3_red] s_tl2=TL_RED -> (s_tl2'=TL_RED);

	[p8_1_red] s_tl2=TL_GREEN -> (s_tl2'=TL_RED);		
	[p8_1_red] s_tl2=TL_RED -> (s_tl2'=TL_RED);		

	[p8_2_red] s_tl2=TL_GREEN -> (s_tl2'=TL_RED);		
	[p8_2_red] s_tl2=TL_RED -> (s_tl2'=TL_RED);	

	[p8_3_red] s_tl2=TL_GREEN -> (s_tl2'=TL_RED);		
	[p8_3_red] s_tl2=TL_RED -> (s_tl2'=TL_RED);		
endmodule

module tl3
	s_tl3: [0..2] init TL_RED;
	[p1_green] s_tl3=TL_RED -> (s_tl3'=TL_GREEN);
	[p1_green] s_tl3=TL_GREEN -> (s_tl3'=TL_GREEN);

	
	[p2_green] s_tl3=TL_RED -> (s_tl3'=TL_GREEN);
	[p2_green] s_tl3=TL_GREEN -> (s_tl3'=TL_GREEN);

	[p3_green] s_tl3=TL_RED -> (s_tl3'=TL_GREEN);
	[p3_green] s_tl3=TL_GREEN -> (s_tl3'=TL_GREEN);

	[p4_red] s_tl3=TL_RED -> (s_tl3'=TL_RED);
	[p4_red] s_tl3=TL_GREEN -> (s_tl3'=TL_RED);

	[p5_red] s_tl3=TL_RED -> (s_tl3'=TL_RED);
	[p5_red] s_tl3=TL_GREEN -> (s_tl3'=TL_RED);	

	[p6_green] s_tl3=TL_RED -> (s_tl3'=TL_GREEN);
	[p6_green] s_tl3=TL_GREEN -> (s_tl3'=TL_GREEN);	

	[p7_1_red] s_tl3=TL_GREEN -> (s_tl3'=TL_RED);		
	[p7_1_red] s_tl3=TL_RED -> (s_tl3'=TL_RED);	

	[p7_2_red] s_tl3=TL_GREEN -> (s_tl3'=TL_RED);		
	[p7_2_red] s_tl3=TL_RED -> (s_tl3'=TL_RED);	

	[p7_3_red] s_tl3=TL_GREEN -> (s_tl3'=TL_RED);

	[p8_1_red] s_tl3=TL_GREEN -> (s_tl3'=TL_RED);		
	[p8_1_red] s_tl3=TL_RED -> (s_tl3'=TL_RED);

	[p8_2_red] s_tl3=TL_GREEN -> (s_tl3'=TL_RED);		
	[p8_2_red] s_tl3=TL_RED -> (s_tl3'=TL_RED);	

	[p8_3_red] s_tl3=TL_GREEN -> (s_tl3'=TL_RED);		
	[p8_3_red] s_tl3=TL_RED -> (s_tl3'=TL_RED);		
endmodule

module tl4
	s_tl4: [0..2] init TL_RED;
	[p1_green] s_tl4=TL_RED -> (s_tl4'=TL_GREEN);
	[p2_red] s_tl4=TL_GREEN -> (s_tl4'=TL_RED);
	[p2_red] s_tl4=TL_RED -> (s_tl4'=TL_RED);
	
	[p4_green] s_tl4=TL_RED -> (s_tl4'=TL_GREEN);

	[p5_red] s_tl4=TL_GREEN -> (s_tl4'=TL_RED);
	[p5_red] s_tl4=TL_RED -> (s_tl4'=TL_RED);

	[p7_1_red] s_tl4=TL_GREEN -> (s_tl4'=TL_RED);

	[p8_1_red] s_tl4=TL_GREEN -> (s_tl4'=TL_RED);
	[p8_1_red] s_tl4=TL_RED -> (s_tl4'=TL_RED);	
endmodule

module tl5
	s_tl5: [0..2] init TL_RED;
	[p1_red] s_tl5=TL_GREEN -> (s_tl5'=TL_RED);
	[p1_red] s_tl5=TL_RED -> (s_tl5'=TL_RED);

	[p3_green] s_tl5=TL_RED -> (s_tl5'=TL_GREEN);

	[p4_red] s_tl5=TL_GREEN -> (s_tl5'=TL_RED);
	[p4_red] s_tl5=TL_RED -> (s_tl5'=TL_RED);

	[p6_green] s_tl5=TL_RED -> (s_tl5'=TL_GREEN);

	[p7_1_red] s_tl5=TL_GREEN -> (s_tl5'=TL_RED);		
	[p7_1_red] s_tl5=TL_RED -> (s_tl5'=TL_RED);
	
	[p8_3_red] s_tl5=TL_GREEN -> (s_tl5'=TL_RED);
	[p8_3_red] s_tl5=TL_RED -> (s_tl5'=TL_RED);

	[p7_3_red] s_tl5=TL_GREEN -> (s_tl5'=TL_RED);	
			
endmodule

module tl6
	s_tl6: [0..2] init TL_RED;
	[p1_green] s_tl6=TL_RED -> (s_tl6'=TL_GREEN);
	[p1_green] s_tl6=TL_GREEN -> (s_tl6'=TL_GREEN);

	[p2_green] s_tl6=TL_RED -> (s_tl6'=TL_GREEN);
	[p2_green] s_tl6=TL_GREEN -> (s_tl6'=TL_GREEN);

	[p3_green] s_tl6=TL_RED -> (s_tl6'=TL_GREEN);
	[p3_green] s_tl6=TL_GREEN -> (s_tl6'=TL_GREEN);

	[p4_red] s_tl6=TL_RED -> (s_tl6'=TL_RED);
	[p4_red] s_tl6=TL_GREEN -> (s_tl6'=TL_RED);

	[p5_green] s_tl6=TL_RED -> (s_tl6'=TL_GREEN);
	[p5_green] s_tl6=TL_GREEN -> (s_tl6'=TL_GREEN);

	[p6_red] s_tl6=TL_RED -> (s_tl6'=TL_RED);
	[p6_red] s_tl6=TL_GREEN -> (s_tl6'=TL_RED);

	[p7_1_red] s_tl6=TL_GREEN -> (s_tl6'=TL_RED);		
	[p7_1_red] s_tl6=TL_RED -> (s_tl6'=TL_RED);

	[p7_2_red] s_tl6=TL_GREEN -> (s_tl6'=TL_RED);		

	[p7_3_red] s_tl6=TL_GREEN -> (s_tl6'=TL_RED);		
	[p7_3_red] s_tl6=TL_RED -> (s_tl6'=TL_RED);

	[p8_1_red] s_tl6=TL_GREEN -> (s_tl6'=TL_RED);		
	[p8_1_red] s_tl6=TL_RED -> (s_tl6'=TL_RED);

	[p8_2_red] s_tl6=TL_GREEN -> (s_tl6'=TL_RED);		
	[p8_2_red] s_tl6=TL_RED -> (s_tl6'=TL_RED);	

	[p8_3_red] s_tl6=TL_GREEN -> (s_tl6'=TL_RED);		
	[p8_3_red] s_tl6=TL_RED -> (s_tl6'=TL_RED);					
endmodule

module tl7
	s_tl7: [0..2] init TL_RED;		
	[p8_1_green] s_tl7=TL_RED -> (s_tl7'=TL_GREEN);
	[p8_2_green] s_tl7=TL_RED -> (s_tl7'=TL_GREEN);
	[p8_3_green] s_tl7=TL_RED -> (s_tl7'=TL_GREEN);

	[p1_red] s_tl7=TL_GREEN -> (s_tl7'=TL_RED);
	[p1_red] s_tl7=TL_RED -> (s_tl7'=TL_RED);

	[p2_red] s_tl7=TL_GREEN -> (s_tl7'=TL_RED);
	[p2_red] s_tl7=TL_RED -> (s_tl7'=TL_RED);

	[p3_red] s_tl7=TL_GREEN -> (s_tl7'=TL_RED);
	[p3_red] s_tl7=TL_RED -> (s_tl7'=TL_RED);

	[p4_red] s_tl7=TL_GREEN -> (s_tl7'=TL_RED);
	[p4_red] s_tl7=TL_RED -> (s_tl7'=TL_RED);

	[p5_red] s_tl7=TL_GREEN -> (s_tl7'=TL_RED);
	[p5_red] s_tl7=TL_RED -> (s_tl7'=TL_RED);

	[p6_red] s_tl7=TL_GREEN -> (s_tl7'=TL_RED);
	[p6_red] s_tl7=TL_RED -> (s_tl7'=TL_RED);
				
endmodule

module pl1
	s_pl1: [0..2] init TL_RED;

	[p1_red] s_pl1=TL_GREEN -> (s_pl1'=TL_RED); // Apres etre passée en 7_3
	[p1_red] s_pl1=TL_RED -> (s_pl1'=TL_RED);

	[p2_red] s_pl1=TL_GREEN -> (s_pl1'=TL_RED);
	[p2_red] s_pl1=TL_RED -> (s_pl1'=TL_RED);

	[p3_red] s_pl1=TL_GREEN -> (s_pl1'=TL_RED);
	[p3_red] s_pl1=TL_RED -> (s_pl1'=TL_RED);

	[p4_red] s_pl1=TL_RED -> (s_pl1'=TL_RED); // au cas ou y a les pompiers
	[p4_red] s_pl1=TL_GREEN -> (s_pl1'=TL_RED);

	[p6_green] s_pl1=TL_RED -> (s_pl1'=TL_GREEN);

	[p7_1_green] s_pl1=TL_RED -> (s_pl1'=TL_GREEN);

	[p7_2_green] s_pl1=TL_RED -> (s_pl1'=TL_GREEN);

	[p7_3_green] s_pl1=TL_RED -> (s_pl1'=TL_GREEN);
	[p7_3_green] s_pl1=TL_GREEN -> (s_pl1'=TL_GREEN);

	[p8_1_red] s_pl1=TL_GREEN -> (s_pl1'=TL_RED);
	[p8_1_red] s_pl1=TL_RED -> (s_pl1'=TL_RED);

	[p8_2_red] s_pl1=TL_GREEN -> (s_pl1'=TL_RED);
	[p8_2_red] s_pl1=TL_RED -> (s_pl1'=TL_RED);

	[p8_3_red] s_pl1=TL_GREEN -> (s_pl1'=TL_RED);
	[p8_3_red] s_pl1=TL_RED -> (s_pl1'=TL_RED);
endmodule

module pl2
	s_pl2: [0..2] init TL_RED;

	
	[p1_red] s_pl2=TL_GREEN -> (s_pl2'=TL_RED); // Apres etre passée en 7_3
	[p1_red] s_pl2=TL_RED -> (s_pl2'=TL_RED);

	[p2_red] s_pl2=TL_GREEN -> (s_pl2'=TL_RED);
	[p2_red] s_pl2=TL_RED -> (s_pl2'=TL_RED);

	[p3_red] s_pl2=TL_GREEN -> (s_pl2'=TL_RED);
	[p3_red] s_pl2=TL_RED -> (s_pl2'=TL_RED);
	
	[p4_green] s_pl2=TL_RED -> (s_pl2'=TL_GREEN);
	[p4_green] s_pl2=TL_GREEN -> (s_pl2'=TL_GREEN);

	[p5_red] s_pl2=TL_GREEN -> (s_pl2'=TL_RED);
	[p5_red] s_pl2=TL_RED -> (s_pl2'=TL_RED);

	[p7_1_green] s_pl2=TL_RED -> (s_pl2'=TL_GREEN);
	[p7_1_green] s_pl2=TL_GREEN -> (s_pl2'=TL_GREEN);

	[p7_2_green] s_pl2=TL_RED -> (s_pl2'=TL_GREEN);

	[p7_3_green] s_pl2=TL_RED -> (s_pl2'=TL_GREEN);

	[p8_1_red] s_pl2=TL_GREEN -> (s_pl2'=TL_RED);
	[p8_1_red] s_pl2=TL_RED -> (s_pl2'=TL_RED);

	[p8_2_red] s_pl2=TL_GREEN -> (s_pl2'=TL_RED);
	[p8_2_red] s_pl2=TL_RED -> (s_pl2'=TL_RED);

	[p8_3_red] s_pl2=TL_GREEN -> (s_pl2'=TL_RED);
	[p8_3_red] s_pl2=TL_RED -> (s_pl2'=TL_RED);

endmodule

module pl3
	s_pl3: [0..2] init TL_RED;

	[p1_red] s_pl3=TL_RED -> (s_pl3'=TL_RED);
	[p1_red] s_pl3=TL_GREEN -> (s_pl3'=TL_RED);	

	[p2_red] s_pl3=TL_RED -> (s_pl3'=TL_RED);
	[p2_red] s_pl3=TL_GREEN -> (s_pl3'=TL_RED);	

	[p3_red] s_pl3=TL_RED -> (s_pl3'=TL_RED);
	[p3_red] s_pl3=TL_GREEN -> (s_pl3'=TL_RED);	

	[p5_green] s_pl3=TL_RED -> (s_pl3'=TL_GREEN);
	[p5_green] s_pl3=TL_GREEN -> (s_pl3'=TL_GREEN);	

	[p6_red] s_pl3=TL_RED -> (s_pl3'=TL_RED);
	[p6_red] s_pl3=TL_GREEN -> (s_pl3'=TL_RED);	

	[p7_1_green] s_pl3=TL_RED -> (s_pl3'=TL_GREEN);

	[p7_2_green] s_pl3=TL_RED -> (s_pl3'=TL_GREEN);
	[p7_2_green] s_pl3=TL_GREEN -> (s_pl3'=TL_GREEN);

	[p7_3_green] s_pl3=TL_RED -> (s_pl3'=TL_GREEN);

	[p8_1_red] s_pl3=TL_RED -> (s_pl3'=TL_RED);
	[p8_1_red] s_pl3=TL_GREEN -> (s_pl3'=TL_RED);

	[p8_2_red] s_pl3=TL_RED -> (s_pl3'=TL_RED);
	[p8_2_red] s_pl3=TL_GREEN -> (s_pl3'=TL_RED);

	[p8_3_red] s_pl3=TL_GREEN -> (s_pl3'=TL_RED);
	[p8_3_red] s_pl3=TL_RED -> (s_pl3'=TL_RED);		
endmodule


module pb1
	s_pb1: bool init PB_DEACTIVATE;
	[p1_green] s_pb1=PB_DEACTIVATE  -> 0.2: (s_pb1'=PB_ACTIVATE) + 0.8: (s_pb1'=PB_DEACTIVATE);
	[p1_green] s_pb1=PB_ACTIVATE  -> (s_pb1'=PB_ACTIVATE);
	
	[p2_green] s_pb1=PB_DEACTIVATE  -> 0.2: (s_pb1'=PB_ACTIVATE) + 0.8: (s_pb1'=PB_DEACTIVATE);
	[p2_green] s_pb1=PB_ACTIVATE  -> (s_pb1'=PB_ACTIVATE);
	
	[p3_green] s_pb1=PB_DEACTIVATE  -> 0.2: (s_pb1'=PB_ACTIVATE) + 0.8: (s_pb1'=PB_DEACTIVATE);
	[p4_green] s_pb1=PB_DEACTIVATE  -> 0.2: (s_pb1'=PB_ACTIVATE) + 0.8: (s_pb1'=PB_DEACTIVATE);
	[p4_green] s_pb1=PB_ACTIVATE  -> (s_pb1'=PB_ACTIVATE);
	
	[p5_green] s_pb1=PB_DEACTIVATE  -> 0.2: (s_pb1'=PB_ACTIVATE) + 0.8: (s_pb1'=PB_DEACTIVATE);
	[p5_green] s_pb1=PB_ACTIVATE  -> (s_pb1'=PB_ACTIVATE); //car si en phase 1 pb1 est activé on peut pas le retester en phase 2 ou 5

	[p6_red] s_pb1=PB_ACTIVATE  -> (s_pb1'=PB_DEACTIVATE);

	[p7_1_red] s_pb1=PB_DEACTIVATE  -> (s_pb1'=PB_DEACTIVATE);
	[p7_1_red] s_pb1=PB_ACTIVATE  -> (s_pb1'=PB_DEACTIVATE);

	[p7_2_red] s_pb1=PB_DEACTIVATE  -> (s_pb1'=PB_DEACTIVATE);
	[p7_2_red] s_pb1=PB_ACTIVATE  -> (s_pb1'=PB_DEACTIVATE);

	[p7_3_red] s_pb1=PB_DEACTIVATE  -> (s_pb1'=PB_DEACTIVATE);
	[p7_3_red] s_pb1=PB_ACTIVATE  -> (s_pb1'=PB_DEACTIVATE);	
endmodule

module pb2
	s_pb2: bool init PB_DEACTIVATE;
	[p1_green] s_pb2=PB_DEACTIVATE  -> 0.2: (s_pb2'=PB_ACTIVATE) + 0.8: (s_pb2'=PB_DEACTIVATE);
	[p2_green] s_pb2=PB_DEACTIVATE  -> 0.2: (s_pb2'=PB_ACTIVATE) + 0.8: (s_pb2'=PB_DEACTIVATE);
	[p2_green] s_pb2=PB_ACTIVATE  -> (s_pb2'=PB_ACTIVATE);
	
	[p3_green] s_pb2=PB_DEACTIVATE  -> 0.2: (s_pb2'=PB_ACTIVATE) + 0.8: (s_pb2'=PB_DEACTIVATE);
	[p3_green] s_pb2=PB_ACTIVATE  -> (s_pb2'=PB_ACTIVATE);
		
	[p5_green] s_pb2=PB_DEACTIVATE  -> 0.2: (s_pb2'=PB_ACTIVATE) + 0.8: (s_pb2'=PB_DEACTIVATE);
	[p5_green] s_pb2=PB_ACTIVATE  -> (s_pb2'=PB_ACTIVATE);
	
	[p6_green] s_pb2=PB_DEACTIVATE  -> 0.2: (s_pb2'=PB_ACTIVATE) + 0.8: (s_pb2'=PB_DEACTIVATE);
	[p6_green] s_pb2=PB_ACTIVATE  -> (s_pb2'=PB_ACTIVATE);

	[p4_red] s_pb2=PB_ACTIVATE -> (s_pb2'=PB_DEACTIVATE);
	
	[p7_1_red] s_pb2=PB_DEACTIVATE  -> (s_pb2'=PB_DEACTIVATE);
	[p7_1_red] s_pb2=PB_ACTIVATE  -> (s_pb2'=PB_DEACTIVATE);

	[p7_2_red] s_pb2=PB_DEACTIVATE  -> (s_pb2'=PB_DEACTIVATE);
	[p7_2_red] s_pb2=PB_ACTIVATE  -> (s_pb2'=PB_DEACTIVATE);

	[p7_3_red] s_pb2=PB_DEACTIVATE  -> (s_pb2'=PB_DEACTIVATE);
	[p7_3_red] s_pb2=PB_ACTIVATE  -> (s_pb2'=PB_DEACTIVATE);	
endmodule

module pb3
	s_pb3: bool init PB_DEACTIVATE;
	[p1_green] s_pb3=PB_DEACTIVATE  -> 0.2: (s_pb3'=PB_ACTIVATE) + 0.8: (s_pb3'=PB_DEACTIVATE);
	[p1_green] s_pb3=PB_ACTIVATE  -> (s_pb3'=PB_ACTIVATE);
	
	[p2_green] s_pb3=PB_DEACTIVATE  -> 0.2: (s_pb3'=PB_ACTIVATE) + 0.8: (s_pb3'=PB_DEACTIVATE);
	
	[p3_green] s_pb3=PB_DEACTIVATE  -> 0.2: (s_pb3'=PB_ACTIVATE) + 0.8: (s_pb3'=PB_DEACTIVATE);
	[p3_green] s_pb3=PB_ACTIVATE  -> (s_pb3'=PB_ACTIVATE); // Si en phase 2 , pb3 est activé, faut pas le retester en phase 3 ou 6

	[p4_green] s_pb3=PB_DEACTIVATE  -> 0.2: (s_pb3'=PB_ACTIVATE) + 0.8: (s_pb3'=PB_DEACTIVATE);
	[p4_green] s_pb3=PB_ACTIVATE  -> (s_pb3'=PB_ACTIVATE);
		
	[p6_green] s_pb3=PB_DEACTIVATE  -> 0.2: (s_pb3'=PB_ACTIVATE) + 0.8: (s_pb3'=PB_DEACTIVATE);
	[p6_green] s_pb3=PB_ACTIVATE  -> (s_pb3'=PB_ACTIVATE);

	[p5_red] s_pb3=PB_ACTIVATE  -> (s_pb3'=PB_DEACTIVATE);

	[p7_1_red] s_pb3=PB_DEACTIVATE  -> (s_pb3'=PB_DEACTIVATE);
	[p7_1_red] s_pb3=PB_ACTIVATE  -> (s_pb3'=PB_DEACTIVATE);

	[p7_2_red] s_pb3=PB_DEACTIVATE  -> (s_pb3'=PB_DEACTIVATE);
	[p7_2_red] s_pb3=PB_ACTIVATE  -> (s_pb3'=PB_DEACTIVATE);

	[p7_3_red] s_pb3=PB_DEACTIVATE  -> (s_pb3'=PB_DEACTIVATE);
	[p7_3_red] s_pb3=PB_ACTIVATE  -> (s_pb3'=PB_DEACTIVATE);
endmodule

module fire
	s_fire: bool init false;
	[p1_green] s_fire=NO  -> 0.02: (s_fire'=YES) + 0.98: (s_fire'=NO);
	[p2_green] s_fire=NO  -> 0.02: (s_fire'=YES) + 0.98: (s_fire'=NO);
	[p3_green] s_fire=NO  -> 0.02: (s_fire'=YES) + 0.98: (s_fire'=NO);
	[p4_green] s_fire=NO  -> 0.02: (s_fire'=YES) + 0.98: (s_fire'=NO);
	[p5_green] s_fire=NO  -> 0.02: (s_fire'=YES) + 0.98: (s_fire'=NO);
	[p6_green] s_fire=NO  -> 0.02: (s_fire'=YES) + 0.98: (s_fire'=NO);
	[p7_1_green] s_fire=NO  -> 0.02: (s_fire'=YES) + 0.98: (s_fire'=NO);
	[p7_2_green] s_fire=NO  -> 0.02: (s_fire'=YES) + 0.98: (s_fire'=NO);
	[p7_3_green] s_fire=NO  -> 0.02: (s_fire'=YES) + 0.98: (s_fire'=NO);

	[p8_1_red] s_fire=YES  -> (s_fire'=NO);
	[p8_2_red] s_fire=YES  -> (s_fire'=NO);
	[p8_3_red] s_fire=YES  -> (s_fire'=NO);
endmodule
