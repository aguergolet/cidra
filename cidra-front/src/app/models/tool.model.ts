export class Tool {
    id: string = '';
    title: string = '';
    description: string = '';
    output: ToolOutput = new ToolOutput(); 
    params: ToolParams[] = [];
}

export class ToolOutput {
    description: string = '';
}

export class ToolParams {
    name: string = '';
    type: string = '';
    title: string = '';
    description: string = '';
    required: boolean = false;
    default: string = '';
    value: string = ''
}